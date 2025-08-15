# AI Image Generation Prompt Engineering Guide

## Core Principles

### Structure for Effective Prompts
```
[Subject] + [Medium] + [Style] + [Lighting] + [Composition] + [Quality Modifiers]
```

**Example:**
"Professional product photography of black hoodie, studio lighting, white background, commercial quality, high resolution, centered composition"

### Essential Elements

1. **Subject Description** (Required)
   - What you want to generate
   - Be specific about details that matter
   - Use precise terminology

2. **Medium/Format** (Important)
   - Photography, illustration, digital art, painting
   - Specific camera or artistic medium references

3. **Style/Aesthetic** (Varies by use case)
   - Art movement, specific artist style, era
   - Color palette, mood, atmosphere

4. **Technical Specifications** (Critical for commercial use)
   - Lighting setup, camera settings
   - Background, composition, quality

## E-commerce Specific Prompts

### Product Photography Templates

#### Clean Product Shots
```
Professional product photography of [PRODUCT], 
clean white background, studio lighting, sharp focus, 
high resolution, commercial quality, no shadows, 
centered composition, 85mm lens
```

#### Lifestyle Product Images
```
[PERSON] wearing [PRODUCT] in [SETTING], 
natural lighting, lifestyle photography, 
authentic moment, high quality, candid shot
```

#### Hero/Banner Images
```
Premium [PRODUCT] displayed elegantly, 
luxury presentation, dramatic lighting, 
sophisticated composition, marketing quality
```

### Testimonial/Review Image Templates

#### Authentic Customer Photos
```
Real person holding [PRODUCT], genuine smile, 
natural lighting, authentic customer photo, 
casual setting, smartphone photo quality
```

#### TikTok-Style Content
```
Young person showcasing [PRODUCT], 
trendy aesthetic, good lighting, social media style, 
engaging pose, modern background
```

#### Professional Testimonials
```
Professional headshot style photo of person with [PRODUCT], 
confident expression, business casual attire, 
clean background, high quality portrait
```

## Platform-Specific Optimization

### OpenAI DALL-E 3 / GPT Image
**Strengths:** Instruction following, text integration, photorealism
```
[Detailed description] + professional photography + 
studio lighting + commercial quality + specific background
```

**Example:**
```
"Professional e-commerce photo of premium black hoodie 
displayed on invisible mannequin, studio lighting with 
soft shadows, clean white background, commercial photography, 
high resolution, crisp details, centered composition"
```

### Midjourney
**Strengths:** Artistic quality, style consistency, creative interpretation
```
[Subject] + [artistic style] + [quality modifiers] + [parameters]
```

**Example:**
```
"Black hoodie product shot, professional photography, 
clean aesthetic, minimalist style --ar 1:1 --q 2 --s 750"
```

### Stable Diffusion
**Strengths:** Customization, cost-effectiveness, open source flexibility
```
[Subject] + [detailed description] + [style] + [technical specs] + [quality]
```

**Example:**
```
"Professional product photograph of black hoodie, white background, 
studio lighting, commercial photography, high resolution, sharp focus, 
no shadows, clean presentation"

Negative prompt: "blurry, low quality, distorted, watermark, text, shadows"
```

### FLUX Models
**Strengths:** Prompt adherence, photorealism, commercial quality
```
[Specific subject] + [professional context] + [technical requirements]
```

**Example:**
```
"E-commerce product photo of black hoodie, professional studio setup, 
seamless white background, even lighting, commercial photography standards, 
high detail, crisp focus"
```

## Advanced Prompt Techniques

### Multi-Prompt Weighting (Stable Diffusion)
```python
# Emphasize important elements
prompt = """
(professional photography:1.3), black hoodie, 
(studio lighting:1.2), white background, 
(commercial quality:1.4), high resolution
"""
```

### Negative Prompting
```python
negative_prompt = """
blurry, low quality, amateur, distorted, watermark, 
text, logo, shadows, wrinkled, poor lighting, 
oversaturated, undersaturated
"""
```

### Style Transfer Techniques
```
"In the style of [reference], [subject description], 
maintaining [specific characteristics]"
```

## Quality Enhancement Keywords

### Photography Terms
- Professional photography
- Studio lighting
- Commercial quality  
- High resolution
- Sharp focus
- Crisp details
- Perfect exposure
- Color accurate

### Composition Terms
- Centered composition
- Rule of thirds
- Symmetrical layout
- Balanced framing
- Clean background
- Minimal design
- Product focus

### Lighting Descriptors
- Studio lighting
- Soft box lighting
- Natural lighting
- Even illumination
- No harsh shadows
- Bright and airy
- Professional setup

### Quality Modifiers
- Ultra high quality
- 4K resolution
- Commercial grade
- Professional standard
- Crisp and clean
- Perfect clarity
- Studio quality

## Common Mistakes to Avoid

### Over-Specification
❌ "Show me a picture of a large, oversized, big, huge black hoodie with long sleeves..."
✅ "Oversized black hoodie, professional product photo"

### Negative Language
❌ "Black hoodie without wrinkles, no bad lighting, not blurry"
✅ "Black hoodie, smooth fabric, studio lighting, sharp focus"

### Conflicting Instructions
❌ "Casual lifestyle photo with professional studio lighting"
✅ "Lifestyle photo with natural lighting" OR "Studio photo with professional lighting"

### Unclear Subjects
❌ "Nice looking clothes"
✅ "Premium black hoodie, front view"

## Testing and Iteration

### A/B Testing Prompts
1. Generate multiple versions with slight prompt variations
2. Compare results for consistency and quality
3. Identify which elements produce best results
4. Refine and standardize successful patterns

### Prompt Evolution Process
```python
# Version 1 (Basic)
prompt_v1 = "Black hoodie, white background"

# Version 2 (Enhanced)  
prompt_v2 = "Black hoodie, professional product photo, white background"

# Version 3 (Optimized)
prompt_v3 = "Professional e-commerce photo of premium black hoodie, 
studio lighting, seamless white background, commercial quality"
```

### Quality Assessment Criteria
- **Consistency**: Similar results across generations
- **Accuracy**: Matches intended description
- **Quality**: Professional appearance suitable for use
- **Brand Alignment**: Fits overall aesthetic requirements

## Platform-Specific Parameters

### Midjourney Parameters
```
--ar 1:1          # Square aspect ratio
--q 2             # High quality
--s 750           # Medium stylization
--c 10            # Low chaos/variation
--no text,logo    # Exclude elements
```

### Stable Diffusion Parameters
```python
{
    "guidance_scale": 7.5,      # Prompt adherence
    "num_inference_steps": 50,  # Quality vs speed
    "width": 1024,              # Image width
    "height": 1024,             # Image height
    "scheduler": "DPMSolver++"  # Generation algorithm
}
```

### FLUX Parameters
```python
{
    "aspect_ratio": "1:1",
    "output_format": "png",
    "output_quality": 100,
    "num_outputs": 4,
    "guidance_scale": 3.5
}
```

## Batch Generation Strategies

### Systematic Variations
```python
base_prompt = "Professional product photo of {} hoodie"
variations = [
    "black premium", "black casual", "black luxury",
    "navy premium", "gray premium", "white premium"
]

prompts = [base_prompt.format(var) for var in variations]
```

### Multi-Angle Product Shots
```python
angles = ["front view", "side view", "back view", "three-quarter view"]
base = "Professional product photo of black hoodie, {}, white background, studio lighting"

angle_prompts = [base.format(angle) for angle in angles]
```

### Seasonal/Context Variations
```python
contexts = [
    "studio photography setup",
    "outdoor natural lighting", 
    "modern interior setting",
    "minimalist display"
]
```