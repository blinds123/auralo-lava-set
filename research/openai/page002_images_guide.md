# OpenAI Images and Vision API Documentation

**URL Source:** https://platform.openai.com/docs/guides/images

## Overview

The OpenAI API offers several endpoints to process images as input or generate them as output, enabling you to build powerful multimodal applications.

### API Endpoints for Images

| API | Supported use cases |
|-----|-------------------|
| [Responses API](https://platform.openai.com/docs/api-reference/responses) | Analyze images and use them as input and/or generate images as output |
| [Images API](https://platform.openai.com/docs/api-reference/images) | Generate images as output, optionally using images as input |
| [Chat Completions API](https://platform.openai.com/docs/api-reference/chat) | Analyze images and use them as input to generate text or audio |

## Image Generation

### Latest Model: GPT Image 1
Our latest image generation model, `gpt-image-1`, is a natively multimodal large language model. It can understand text and images and leverage its broad world knowledge to generate images with better instruction following and contextual awareness.

### Example Code for Image Generation
```python
from openai import OpenAI
import base64

client = OpenAI() 

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Generate an image of gray tabby cat hugging an otter with an orange scarf",
    tools=[{"type": "image_generation"}],
)

# Save the image to a file
image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]

if image_data:
    image_base64 = image_data[0]
    with open("cat_and_otter.png", "wb") as f:
        f.write(base64.b64decode(image_base64))
```

### World Knowledge for Image Generation
The difference between DALL·E models and GPT Image is that a natively multimodal language model can use its visual understanding of the world to generate lifelike images including real-life details without a reference.

## Image Analysis (Vision)

**Vision** is the ability for a model to "see" and understand images. Models can understand most visual elements, including objects, shapes, colors, and textures.

### Image Input Methods
You can provide images as input in multiple ways:
- By providing a fully qualified URL to an image file
- By providing an image as a Base64-encoded data URL
- By providing a file ID (created with the Files API)

### Example: Passing Image URL
```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": "what's in this image?"},
            {
                "type": "input_image",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            },
        ],
    }],
)

print(response.output_text)
```

## Image Input Requirements

### Supported File Types
- PNG (.png)
- JPEG (.jpeg and .jpg)
- WEBP (.webp)
- Non-animated GIF (.gif)

### Size Limits
- Up to 50 MB total payload size per request
- Up to 500 individual image inputs per request

### Other Requirements
- No watermarks or logos
- No NSFW content
- Clear enough for a human to understand

## Detail Level Parameter

The `detail` parameter controls processing level:
- `"low"`: 85 tokens budget, 512px x 512px processing
- `"high"`: Better understanding with higher token cost
- `"auto"`: Let the model decide (default)

```json
{
    "type": "input_image",
    "image_url": "https://example.com/image.jpg",
    "detail": "high"
}
```

## Vision Model Limitations

- **Medical images**: Not suitable for CT scans or medical advice
- **Non-English**: May not perform optimally with non-Latin alphabets
- **Small text**: Enlarge text for better readability
- **Rotation**: May misinterpret rotated/upside-down content
- **Visual elements**: Struggles with graphs using different line styles
- **Spatial reasoning**: Difficulty with precise spatial localization
- **Accuracy**: May generate incorrect descriptions in some scenarios
- **Image shape**: Struggles with panoramic and fisheye images
- **Metadata**: Doesn't process original filenames or metadata
- **Counting**: May give approximate counts for objects
- **CAPTCHAs**: Blocked for safety reasons

## Cost Calculation

### GPT-4.1-mini, GPT-4.1-nano, o4-mini
Image cost based on 32px x 32px patches:

1. Calculate patches needed: `ceil(width/32) × ceil(height/32)`
2. If patches > 1536, scale down image
3. Token cost = number of patches (max 1536)
4. Apply model multiplier:

| Model | Multiplier |
|-------|-----------|
| gpt-5-mini | 1.62 |
| gpt-5-nano | 2.46 |
| gpt-4.1-mini | 1.62 |
| gpt-4.1-nano | 2.46 |
| o4-mini | 1.72 |

### GPT 4o, GPT-4.1, o-series Models
Cost determined by size and detail level:

| Model | Base tokens | Tile tokens |
|-------|------------|-------------|
| gpt-5, gpt-5-chat-latest | 70 | 140 |
| 4o, 4.1, 4.5 | 85 | 170 |
| 4o-mini | 2833 | 5667 |
| o1, o1-pro, o3 | 75 | 150 |
| computer-use-preview | 65 | 129 |

### GPT Image 1
- Uses 512px shortest side instead of 768px
- Base cost: 65 image tokens (low fidelity)
- Tile cost: 129 image tokens (low fidelity)
- High fidelity adds extra tokens based on aspect ratio:
  - Square: +4096 tokens
  - Portrait/landscape: +6144 tokens

## Pricing Resources
- Use the image pricing calculator at [openai.com/api/pricing](https://openai.com/api/pricing/)
- Images count toward tokens per minute (TPM) limits