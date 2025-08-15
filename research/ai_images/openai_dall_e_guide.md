# OpenAI DALL-E 3 & GPT Image - Image Generation Guide

## Overview
OpenAI offers several models for image generation and analysis through multiple APIs:

### Available Models
1. **GPT Image 1** - Latest multimodal model with superior instruction following
2. **DALL-E 3** - High-quality specialized image generation 
3. **DALL-E 2** - Lower cost option with concurrent requests and inpainting

### API Options
- **Images API**: Direct image generation, editing, variations
- **Responses API**: Conversational image generation with multi-turn editing

## Key Features

### GPT Image 1 (Recommended)
- **Superior instruction following** - Uses world knowledge for realistic details
- **Text rendering capabilities** - Improved over DALL-E series
- **Multi-turn editing** - Iterative improvements through conversation
- **High input fidelity** - Better preservation of input image details
- **Transparent backgrounds** - Supports PNG/WebP with alpha channel
- **Streaming support** - Partial image generation

### Image Generation Capabilities
- Generate from text prompts
- Edit existing images with masks (inpainting)  
- Create variations of images
- Use multiple input images as references
- Batch generation (multiple images per request)

## Pricing Structure

### GPT Image 1 Token Costs
| Quality | Square (1024×1024) | Portrait (1024×1536) | Landscape (1536×1024) |
|---------|-------------------|----------------------|----------------------|
| Low     | 272 tokens        | 408 tokens           | 400 tokens           |
| Medium  | 1056 tokens       | 1584 tokens          | 1568 tokens          |
| High    | 4160 tokens       | 6240 tokens          | 6208 tokens          |

### DALL-E Pricing
- **DALL-E 3**: $0.040 per 1024×1024 image, $0.080 per 1024×1536/1536×1024 image
- **DALL-E 2**: $0.020 per 1024×1024 image, lower resolutions available

### Additional Costs
- Input text tokens for prompts
- Input image tokens when editing (varies by resolution and detail level)
- Partial images cost 100 additional tokens each

## Technical Specifications

### Image Sizes
- **Standard**: 1024×1024 (square)
- **Portrait**: 1024×1536 
- **Landscape**: 1536×1024
- **Quality**: Low, Medium, High, Auto
- **Format**: PNG (default), JPEG, WebP
- **Compression**: 0-100% for JPEG/WebP

### Input Requirements
- **File types**: PNG, JPEG, WebP, non-animated GIF
- **Size limit**: 50MB total payload per request
- **Max images**: 500 individual inputs per request
- **Requirements**: No watermarks, NSFW content, must be human-readable

### Image Token Calculation
For GPT-4.1-mini, GPT-4.1-nano, o4-mini:
1. Calculate patches needed (32px × 32px patches)
2. Scale down if exceeds 1536 patches
3. Apply model multiplier (1.62x for GPT-4.1-mini)

## Implementation Examples

### Basic Generation (Python)
```python
from openai import OpenAI
import base64

client = OpenAI()

# Using Responses API
response = client.responses.create(
    model="gpt-5",
    input="Generate a professional product photo of a black hoodie",
    tools=[{"type": "image_generation"}],
)

# Save image
image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]

if image_data:
    with open("product_photo.png", "wb") as f:
        f.write(base64.b64decode(image_data[0]))
```

### Advanced Configuration
```python
# High-quality with custom settings
response = client.responses.create(
    model="gpt-5",
    input="Professional e-commerce photo of luxury hoodie",
    tools=[{
        "type": "image_generation",
        "quality": "high",
        "size": "1024x1024",
        "background": "transparent",
        "output_format": "png"
    }],
)
```

### Batch Generation
```python
# Generate multiple variations
prompts = [
    "Black hoodie front view, white background",
    "Black hoodie side view, white background", 
    "Black hoodie back view, white background"
]

images = []
for prompt in prompts:
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024",
        quality="hd"
    )
    images.append(response.data[0].url)
```

## Best Practices

### Prompt Engineering
- **Be specific** about desired style, lighting, composition
- **Include technical details**: "professional product photography", "studio lighting"
- **Specify background**: "clean white background", "transparent background"
- **Mention quality**: "high resolution", "crisp details", "commercial quality"

### E-commerce Applications
- Product photography with consistent backgrounds
- Lifestyle images showing products in use
- Testimonial photos (with ethical considerations)
- Marketing visuals and social media content

### Quality Optimization
- Use "high" quality setting for final images
- Specify exact dimensions needed
- Use PNG for transparency requirements
- Consider batch generation for variations

## Content Moderation
- Built-in NSFW content filter
- `moderation` parameter options: "auto" (default), "low"
- All prompts filtered according to usage policies

## Limitations
- **Latency**: Complex prompts may take up to 2 minutes
- **Text rendering**: Still challenging for precise text placement
- **Consistency**: May struggle with recurring characters across generations
- **Composition**: Difficulty with precise element positioning