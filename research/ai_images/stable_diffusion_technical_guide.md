# Stable Diffusion Technical Guide

## Architecture Overview

Stable Diffusion is a latent diffusion model that operates in a compressed latent space rather than directly on pixels, making it more efficient than traditional diffusion models.

### Core Components

1. **Variational Autoencoder (VAE)**
   - **Encoder**: Compresses 512×512 images to 64×64 latent representations
   - **Decoder**: Reconstructs images from latent space
   - **Compression ratio**: 8×8 = 64x reduction in spatial dimensions
   - **Latent dimensions**: 4 channels instead of 3 RGB channels

2. **U-Net Diffusion Model**
   - **Architecture**: Encoder-decoder with skip connections
   - **Input**: Noisy latent representations + text embeddings
   - **Output**: Predicted noise residual
   - **Conditioning**: Cross-attention layers for text guidance

3. **Text Encoder (CLIP)**
   - **Model**: ViT-L/14 transformer
   - **Input**: Text prompts up to 77 tokens
   - **Output**: 768-dimensional embeddings per token
   - **Frozen weights**: Pre-trained, not updated during training

## Technical Specifications

### Model Versions
- **v1.1**: 237k steps at 256×256, then 194k at 512×512
- **v1.2**: Additional 515k steps with improved aesthetics
- **v1.3**: Added 10% text dropout for better classifier-free guidance
- **v1.4**: Most commonly used version
- **v1.5**: Enhanced version with better quality

### Training Details
- **Dataset**: LAION-5B subset (English descriptions)
- **Hardware**: 32×8×A100 GPUs (256 total GPUs)
- **Batch size**: 2048
- **Optimizer**: AdamW
- **Learning rate**: Warmup to 0.0001, then constant
- **Training time**: ~150,000 GPU hours

## Implementation with Diffusers

### Installation
```bash
pip install diffusers==0.10.2 transformers scipy ftfy accelerate torch
```

### Basic Usage
```python
from diffusers import StableDiffusionPipeline
import torch

# Load model
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float16  # For GPU memory efficiency
)
pipe.to("cuda")

# Generate image
prompt = "Professional product photo of black hoodie, white background"
image = pipe(prompt).images[0]
image.save("product.png")
```

### Advanced Configuration
```python
# Custom pipeline components
from transformers import CLIPTextModel, CLIPTokenizer
from diffusers import AutoencoderKL, UNet2DConditionModel, LMSDiscreteScheduler

# Load components separately
vae = AutoencoderKL.from_pretrained("CompVis/stable-diffusion-v1-4", subfolder="vae")
tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-large-patch14")
text_encoder = CLIPTextModel.from_pretrained("openai/clip-vit-large-patch14")
unet = UNet2DConditionModel.from_pretrained("CompVis/stable-diffusion-v1-4", subfolder="unet")

# Custom scheduler
scheduler = LMSDiscreteScheduler(
    beta_start=0.00085, 
    beta_end=0.012, 
    beta_schedule="scaled_linear", 
    num_train_timesteps=1000
)
```

### Manual Generation Pipeline
```python
import torch
from tqdm import tqdm

# Parameters
height, width = 512, 512
num_inference_steps = 50
guidance_scale = 7.5
generator = torch.manual_seed(42)

# Encode prompt
text_input = tokenizer(
    prompt, 
    padding="max_length", 
    max_length=tokenizer.model_max_length,
    truncation=True, 
    return_tensors="pt"
)
text_embeddings = text_encoder(text_input.input_ids.to("cuda"))[0]

# Unconditional embeddings for CFG
uncond_input = tokenizer(
    [""], 
    padding="max_length", 
    max_length=text_input.input_ids.shape[-1], 
    return_tensors="pt"
)
uncond_embeddings = text_encoder(uncond_input.input_ids.to("cuda"))[0]

# Combine embeddings
text_embeddings = torch.cat([uncond_embeddings, text_embeddings])

# Initialize random latents
latents = torch.randn(
    (1, unet.in_channels, height // 8, width // 8),
    generator=generator,
).to("cuda")

# Denoising loop
scheduler.set_timesteps(num_inference_steps)
latents = latents * scheduler.init_noise_sigma

for t in tqdm(scheduler.timesteps):
    # Expand latents for classifier-free guidance
    latent_model_input = torch.cat([latents] * 2)
    latent_model_input = scheduler.scale_model_input(latent_model_input, timestep=t)
    
    # Predict noise residual
    with torch.no_grad():
        noise_pred = unet(
            latent_model_input, 
            t, 
            encoder_hidden_states=text_embeddings
        ).sample
    
    # Perform guidance
    noise_pred_uncond, noise_pred_text = noise_pred.chunk(2)
    noise_pred = noise_pred_uncond + guidance_scale * (noise_pred_text - noise_pred_uncond)
    
    # Compute previous noisy sample
    latents = scheduler.step(noise_pred, t, latents).prev_sample

# Decode latents to image
latents = 1 / 0.18215 * latents
with torch.no_grad():
    image = vae.decode(latents).sample

# Convert to PIL
image = (image / 2 + 0.5).clamp(0, 1)
image = image.detach().cpu().permute(0, 2, 3, 1).numpy()
images = (image * 255).round().astype("uint8")
pil_image = Image.fromarray(images[0])
```

## Optimization Techniques

### Memory Optimization
```python
# Enable memory efficient attention
pipe.enable_attention_slicing()

# Enable CPU offloading
pipe.enable_sequential_cpu_offload()

# Use half precision
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    revision="fp16",
    torch_dtype=torch.float16
)
```

### Speed Optimization
```python
# Reduce inference steps (trade quality for speed)
image = pipe(prompt, num_inference_steps=20).images[0]

# Use different schedulers
from diffusers import DPMSolverMultistepScheduler
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

# Compile model (PyTorch 2.0+)
pipe.unet = torch.compile(pipe.unet)
```

### Quality Optimization
```python
# Increase inference steps
image = pipe(prompt, num_inference_steps=100).images[0]

# Adjust guidance scale
image = pipe(prompt, guidance_scale=12.0).images[0]

# Use better scheduler
from diffusers import EulerAncestralDiscreteScheduler
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
```

## Advanced Features

### Image-to-Image Generation
```python
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image

pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float16
).to("cuda")

# Load initial image
init_image = Image.open("initial.png").convert("RGB")
init_image = init_image.resize((512, 512))

# Generate variation
prompt = "A professional product photo of the hoodie with better lighting"
image = pipe(
    prompt=prompt,
    image=init_image,
    strength=0.75,  # How much to change (0.0-1.0)
    guidance_scale=7.5
).images[0]
```

### Inpainting
```python
from diffusers import StableDiffusionInpaintPipeline

pipe = StableDiffusionInpaintPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float16
).to("cuda")

# Load image and mask
image = Image.open("product.png").resize((512, 512))
mask_image = Image.open("mask.png").resize((512, 512))

# Inpaint
result = pipe(
    prompt="Professional studio lighting on the product",
    image=image,
    mask_image=mask_image,
    guidance_scale=7.5
).images[0]
```

### ControlNet Integration
```python
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
import cv2
import numpy as np

# Load ControlNet
controlnet = ControlNetModel.from_pretrained(
    "lllyasviel/sd-controlnet-canny",
    torch_dtype=torch.float16
)

pipe = StableDiffusionControlNetPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    controlnet=controlnet,
    torch_dtype=torch.float16
).to("cuda")

# Process control image
image = Image.open("reference.png")
image_np = np.array(image)
canny_image = cv2.Canny(image_np, 100, 200)
control_image = Image.fromarray(canny_image)

# Generate with control
result = pipe(
    prompt="Professional product photo",
    image=control_image,
    guidance_scale=7.5
).images[0]
```

## Performance Considerations

### Hardware Requirements
- **Minimum GPU**: 6GB VRAM (with optimizations)
- **Recommended GPU**: 12GB+ VRAM for full resolution
- **CPU**: Multi-core recommended for preprocessing
- **RAM**: 16GB+ system memory
- **Storage**: SSD recommended for model loading

### Batch Processing
```python
# Generate multiple images efficiently
prompts = [
    "Product photo front view",
    "Product photo side view", 
    "Product photo back view"
]

images = pipe(
    prompts,
    num_images_per_prompt=1,
    guidance_scale=7.5
).images
```

### Environmental Impact
- **Training emissions**: ~11,250 kg CO2 eq for original model
- **Inference efficiency**: Latent space processing reduces compute
- **Energy considerations**: GPU usage for generation
- **Optimization importance**: Efficient inference reduces impact