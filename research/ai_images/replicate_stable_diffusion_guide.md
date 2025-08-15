# Replicate & Stable Diffusion Guide

## Platform Overview
Replicate is a cloud platform for running AI models via API, including various image generation models like Stable Diffusion, FLUX, and proprietary models.

## Popular Image Generation Models on Replicate

### Stable Diffusion Versions
1. **Stable Diffusion 2.1** - Updated fast version with flexible image sizes up to 1024×1024
2. **Stable Diffusion 1.5** - Original optimized version
3. **FLUX.1 Pro** - $0.04 per image, excellent quality and prompt adherence
4. **FLUX.1 Dev** - $0.025 per image, 12B parameter model
5. **FLUX.1 Schnell** - $3.00 per thousand images, fastest generation

### Other Notable Models
- **Ideogram v3 Quality** - $0.09 per image, stunning realism
- **Recraft V3** - $0.04 per image, long text generation, multiple styles
- **Claude 3.7 Sonnet** - Text generation with image analysis

## Pricing Structure

### Hardware-Based Pricing (per second)
| Hardware | Price/sec | Price/hour | GPU | RAM | Use Case |
|----------|-----------|------------|-----|-----|----------|
| CPU Small | $0.000025 | $0.09 | - | 2GB | Light processing |
| GPU T4 | $0.000225 | $0.81 | 1x T4 | 16GB | Basic AI tasks |
| GPU L40S | $0.000975 | $3.51 | 1x L40S | 65GB | Mid-tier generation |
| GPU A100 | $0.001400 | $5.04 | 1x A100 | 144GB | High-end tasks |
| GPU H100 | $0.001525 | $5.49 | 1x H100 | 72GB | Latest hardware |

### Output-Based Pricing Examples
- **FLUX.1 Pro**: $0.04 per image
- **FLUX.1 Dev**: $0.025 per image  
- **FLUX.1 Schnell**: $0.003 per image
- **Ideogram v3**: $0.09 per image
- **Recraft V3**: $0.04 per image

## Implementation Guide

### Python Setup
```python
import replicate

# Set API token
import os
os.environ["REPLICATE_API_TOKEN"] = "your_token_here"

# Or use python-dotenv
from dotenv import load_dotenv
load_dotenv()
```

### Basic Image Generation
```python
# FLUX.1 Pro - High Quality
output = replicate.run(
    "black-forest-labs/flux-1.1-pro",
    input={
        "prompt": "Professional e-commerce photo of black hoodie, white background, studio lighting",
        "aspect_ratio": "1:1",
        "output_format": "png",
        "output_quality": 100
    }
)
```

### Batch Generation
```python
# Generate multiple product views
prompts = [
    "Black hoodie front view, professional product photo, white background",
    "Black hoodie side view, professional product photo, white background", 
    "Black hoodie back view, professional product photo, white background"
]

images = []
for prompt in prompts:
    output = replicate.run(
        "black-forest-labs/flux-dev",
        input={
            "prompt": prompt,
            "num_outputs": 1,
            "aspect_ratio": "1:1",
            "output_format": "png"
        }
    )
    images.extend(output)
```

### Advanced Stable Diffusion Usage
```python
# Stable Diffusion with custom parameters
output = replicate.run(
    "stability-ai/stable-diffusion",
    input={
        "prompt": "A professional product photograph of a luxury black hoodie on white background, studio lighting, high resolution, commercial photography",
        "negative_prompt": "blurry, low quality, distorted, watermark, text, logo",
        "width": 1024,
        "height": 1024,
        "num_inference_steps": 50,
        "guidance_scale": 7.5,
        "scheduler": "DPMSolverMultistep",
        "num_outputs": 4
    }
)
```

## Model Characteristics

### Stable Diffusion Strengths
- **Versatile**: Wide range of styles and subjects
- **Cost-effective**: Multiple pricing tiers available
- **Customizable**: Extensive parameter control
- **Open source**: Transparent and modifiable

### Stable Diffusion Limitations
- **Text rendering**: Cannot render legible text reliably
- **Photorealism**: Not perfect for photographic quality
- **Composition**: Struggles with complex spatial arrangements
- **Consistency**: Faces and people may not generate properly
- **Memory limitations**: Dataset memorization possible

### FLUX Model Advantages
- **Higher quality**: More advanced than Stable Diffusion
- **Better prompt adherence**: Follows instructions more accurately
- **Faster generation**: Especially FLUX Schnell
- **Commercial ready**: Professional quality output

## Best Practices

### Prompt Engineering for Products
```python
# E-commerce optimized prompt
prompt = """
Professional product photography of [PRODUCT], 
clean white background, studio lighting, sharp focus, 
high resolution, commercial quality, no shadows, 
centered composition, 85mm lens, f/8, perfect lighting
"""

# Lifestyle prompt
lifestyle_prompt = """
Person wearing [PRODUCT] in modern urban setting,
natural lighting, lifestyle photography, authentic moment,
high quality, professional photo, real person
"""
```

### Technical Optimization
- **Use negative prompts** to exclude unwanted elements
- **Adjust guidance_scale** (7-15) for prompt adherence
- **Increase inference_steps** (20-100) for quality
- **Choose appropriate scheduler** for generation style
- **Generate multiple outputs** for selection

### Cost Optimization
- **Choose right model** for use case (Schnell for speed, Pro for quality)
- **Batch requests** when possible
- **Use appropriate image sizes** (larger = more expensive)
- **Monitor generation times** for hardware-based pricing

## API Integration

### Webhook Support
```python
# Async generation with webhooks
prediction = replicate.predictions.create(
    version="model_version_id",
    input={"prompt": "your prompt"},
    webhook="https://your-app.com/webhook"
)
```

### File Handling
```python
import requests
from PIL import Image
from io import BytesIO

# Download and process generated images
for image_url in output:
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    
    # Save or process image
    image.save(f"generated_{i}.png")
    
    # Optimize for web
    image.thumbnail((800, 800), Image.Resampling.LANCZOS)
    image.save(f"web_{i}.jpg", "JPEG", quality=85)
```

## Use Cases for E-commerce

### Product Photography
- Clean product shots with consistent backgrounds
- Multiple angle generation for 360° views
- Variation testing for different lighting/angles

### Marketing Materials
- Social media content generation
- Advertisement visuals
- Brand campaign imagery

### Testimonial Content
- Generate diverse customer representations
- Lifestyle scenarios for product use
- Social proof imagery (with ethical considerations)

## Content Policy & Ethics

### Allowed Uses
- Commercial product imagery
- Marketing and advertising content
- Creative and artistic projects
- Educational applications

### Restrictions
- No harmful or illegal content
- No unauthorized person impersonation
- Respect intellectual property rights
- Follow platform community guidelines

### Ethical Considerations
- Transparent about AI-generated content when required
- Avoid misleading representations
- Consider bias in generated imagery
- Respect privacy and consent principles