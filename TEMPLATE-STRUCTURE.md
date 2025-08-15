# 📁 AURALO HOODIE TEMPLATE - DIRECTORY STRUCTURE

## Core Files (Start Here)

### 📌 Essential Reading
- **`AURALO-HOODIE-EXAMPLE.md`** - The complete hoodie formula that made $1M+
- **`QUICK-ADAPTATION-GUIDE.md`** - The 90/10 rule for adaptation
- **`ADAPTATION-WORKFLOW.md`** - Step-by-step process to adapt
- **`START_HERE_PROMPT.md`** - Exact prompt to begin adaptation

### 🎯 Implementation Files
- **`index.html`** - The actual hoodie landing page
- **`sw.js`** - Service worker for performance
- **`netlify.toml`** - Deployment configuration
- **`initial.md`** - Detailed product requirements

## Configuration

### `/config/`
- **`template-config.json`** - All hoodie values and settings
  - Product details (name, prices, tagline)
  - Inventory (47 pieces, XL sellout timing)
  - Payment gateway settings
  - Popup configurations
  - Social proof numbers

- **`placeholders.json`** - Content replacement mappings

## Documentation

### `/documentation/`
- **`russell-brunson-framework.md`** - Hook, Story, Offer psychology
- **`competitive-analysis-framework.md`** - How to analyze competitors
- **`SECTION_ADAPTATION_REQUIREMENTS.md`** - What must stay the same
- **`ADAPTATION_GUIDE.md`** - Technical adaptation details

## Assets

### `/images/product/`
Main product images from the hoodie campaign:
- `main-hoodie.jpg` - Hero product shot
- `bvtryhy_optimized.jpg` - Lifestyle shot 1
- `fggt5cvhj_optimized.jpg` - Lifestyle shot 2
- `fvcf_optimized.jpg` - Lifestyle shot 3
- `morning1_optimized.jpg` - Morning wear shot
- `morning2_optimized.jpg` - Morning wear shot 2
- `vcvjjr_optimized.jpg` - Detail shot

### `/images/story/`
The 7-slide story carousel (Russell Brunson formula):
- `slide-1_final_crushed_under_20kb.jpg` - Hook: "What if you don't need everyone?"
- `slide-2_final_crushed_under_20kb.jpg` - Problem: People pleasing exhaustion
- `slide-3_captioned_final_under_20kb.jpg` - Discovery: Authenticity matters
- `slide-4_final_crushed_under_20kb.jpg` - Journey: 18 months perfecting
- `slide-5_final_crushed_under_20kb.jpg` - Solution: The hoodie introduction
- `slide-6_final_crushed_under_20kb.jpg` - Transformation: 250k joined
- `slide-7_final_crushed_under_20kb.jpg` - CTA: Only 47 left

### `/images/reviews/tiktok/`
10 Gen-Z testimonials (ages 18-27):
- Emma, Sophia, Madison, Ava, Isabella
- Mia, Kristen (all with authentic TikTok style)

### `/images/reviews/trustpilot/`
6 Millennial testimonials (ages 28-35):
- Sarah Mitchell, Lauren White, Emily Thompson
- Danielle Carter, Morgan Hayes, Addison Clarke

### `/images/ui/`
- `auralo-storefront.svg` - Brand logo
- `screenshot1.jpg` - Template preview
- `screenshot2.jpg` - Mobile view

## File Sizes & Performance

All images optimized to <50KB for mobile performance:
- Story slides: ~18-20KB each
- Review images: ~30KB each
- Product images: ~35-45KB each

Total page weight: <2MB (loads in 2.3 seconds)

## What Each File Does

### Must Keep Exactly (90%)
- `index.html` - Core structure and conversion mechanics
- `sw.js` - Performance optimization
- `template-config.json` - Proven values and timings
- All image folders structure - Maintains organization

### Can Customize (10%)
- Product name in config
- Specific testimonial text
- Story slide details (not structure)
- Product images (keep same style)

## Directory Commands

### To start adapting:
```bash
1. cd "Auralo Claude Master Template"
2. Read AURALO-HOODIE-EXAMPLE.md
3. Follow ADAPTATION-WORKFLOW.md
4. Test with: python -m http.server 8000
5. Deploy with: netlify deploy
```

### File naming conventions:
- Reviews: `compressed_[product]_review_[Name]_30kb.jpg`
- Slides: `slide-[number]_final_crushed_under_20kb.jpg`
- Products: `[descriptor]_optimized.jpg`

## Remember

This structure generated $1M+ at 3.2% conversion. Don't reorganize it. The file placement, naming, and organization are all optimized for performance and conversion.