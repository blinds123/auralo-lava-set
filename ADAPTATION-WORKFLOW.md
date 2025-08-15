# 🚀 HOODIE TEMPLATE ADAPTATION WORKFLOW

## The Golden Rule: Keep 90% Exactly, Change 10% Only

## 📋 STEP-BY-STEP PROCESS

### STEP 1: Understand the Hoodie Template (30 min)
```
Read these core files:
• AURALO-HOODIE-EXAMPLE.md - The proven formula
• QUICK-ADAPTATION-GUIDE.md - The 90/10 rule
• index.html - See the actual implementation
• config/template-config.json - The hoodie's values
```

### STEP 2: Analyze Your Product (1 hour)
```
Map your product to the hoodie framework:

1. Price Psychology (Two-Tier System):
   • Hoodie: $200 anchor on BOTH buttons
   • In-Stock: $200 → $99 (Ships immediately)
   • Pre-Order: $200 → $19 (Wait & save)
   • Yours: Keep two-tier structure with your prices

2. Identity Message:
   • Hoodie: "You Are Not For Everyone"
   • Yours: [Your tribal identity statement]

3. Scarcity Story:
   • Hoodie: "Accidentally ordered 500% more"
   • Yours: [Your authentic urgency narrative]

4. Target Audience:
   • Hoodie: Gen-Z/Millennials seeking authenticity
   • Yours: [Your demographic and their pain point]
```

### STEP 3: Generate Assets (2 hours)

#### A. Story Slides (7 Required)
Use the EXACT hoodie structure:
1. Hook: "What if [paradigm shift]?"
2. Problem: "We spent years [wrong approach]..."
3. Discovery: "Then we realized [breakthrough]..."
4. Journey: "[Time] perfecting [mission]..."
5. Solution: "Introducing [product as identity]..."
6. Transformation: "Join [number]+ who [changed]..."
7. CTA: "Only [47] left from [date]..."

#### B. Testimonials (16 Required)
**10 TikTok Reviews (Gen-Z Voice):**
- Ages 18-27
- Lowercase, authentic: "okay but why is this literally..."
- Names: Emma, Sophia, Madison, Ava, Isabella, Mia, Charlotte, Kristen, Olivia, Ashley

**6 Trustpilot Reviews (Millennial Voice):**
- Ages 28-35
- Professional tone with titles
- Names: Sarah Mitchell, Lauren White, Emily Thompson, Danielle Carter, Morgan Hayes, Addison Clarke

#### C. Product Images
- Main hero shot (like main-hoodie.jpg)
- 4-6 lifestyle shots
- All compressed to <50KB

### STEP 4: Update Template (1 hour)

#### Only Change These:
```javascript
// In template-config.json
{
  "product": {
    "name": "[Your Product Name]",
    "tagline": "[Your Identity Message]",
    "originalPrice": [High Anchor - shown on both buttons],
    "inStockPrice": [Immediate delivery price],
    "preorderPrice": [Wait & save price]
  },
  "shipping": {
    "readyToShipTime": "In-Stock: Ready to Ship",
    "preorderShipDate": "Wait & Save: Estimated Ship [Date]"
  }
}
```

#### In index.html:
- Product name occurrences
- Testimonial specific text
- Story slide specific text
- Image file paths

#### DO NOT CHANGE:
- Any popup timing (15 seconds for XL)
- Countdown timer logic
- Value stack structure ($652 total)
- Section order
- Mobile CSS
- JavaScript functions

### STEP 5: Test & Deploy (30 min)

#### Verification Checklist:
- [ ] XL popup triggers at 15 seconds
- [ ] Countdown timer shows time to midnight
- [ ] All 16 testimonials display correctly
- [ ] 7 story slides swipe on mobile
- [ ] Size selector shows "Only X left"
- [ ] Purchase notifications appear
- [ ] Mobile sticky CTA stays at bottom
- [ ] Page loads under 3 seconds
- [ ] All images are <50KB

#### Deploy to Netlify:
```bash
1. Push to GitHub
2. Connect to Netlify
3. Deploy with netlify.toml config
4. Test on real mobile device
```

## 🎯 SUCCESS METRICS

Your adaptation succeeds when you hit the hoodie's numbers:
- **Conversion Rate:** 3.2%
- **Mobile Conversion:** 3.8%
- **Cart Addition:** 8.2%
- **Time on Page:** 4:32
- **Scroll Depth:** 87%

## ⚠️ CRITICAL REMINDERS

### NEVER:
- "Improve" the hoodie's proven elements
- Change popup timing or triggers
- Reduce testimonial count
- Alter the story structure
- Modify checkout flow
- Remove any FOMO elements

### ALWAYS:
- Keep the exact 7-slide format
- Maintain 16 testimonials
- Use the $200→$20 psychology
- Keep "47 pieces" scarcity
- Preserve all animations
- Trust the 3.2% conversion formula

## 💡 Quick Reference

**Hoodie Formula That Works:**
- 15.7M TikTok views story
- 250,000+ social proof
- "You Are Not For Everyone" identity
- Two-button offer ($99 ready vs $19 wait)
- $200 anchor on BOTH buttons
- 47 pieces scarcity
- XL sells out live
- Midnight countdown
- 2-step checkout

**Your Version:**
- [Your viral metric] story
- [Your number]+ social proof
- [Your identity message]
- Two buttons: $[Anchor]→$[InStock] vs $[Anchor]→$[PreOrder]
- 47 pieces (keep this number)
- XL sells out live (keep exactly)
- Midnight countdown (keep exactly)
- 2-step checkout (keep exactly)

---

**Remember:** The hoodie template made $1M+. Don't outsmart it. Copy it.