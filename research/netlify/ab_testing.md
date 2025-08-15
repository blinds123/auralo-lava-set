# Netlify Split Testing (A/B Testing)

## Overview
Branch-based split testing divides traffic between different deploys straight from the CDN without performance impact or third-party JavaScript libraries.

## Requirements & Setup

### Prerequisites
- **Git Repository**: Site must deploy from connected Git repo
- **Branch Deploys**: Must enable branch deploys for test branches
- **Static Content**: Works best with static files, not functions/proxies

### Limitations
- **SSR/ISR Sites**: May cause inconsistent experiences
- **Functions/Proxies**: Not recommended for dynamic content
- **Edge Functions**: Disabled during split testing
- **Scheduled Functions**: Only run on published deploy

## Configuration Process

### 1. Enable Branch Deploys
Navigate to **Project configuration → Build & deploy → Continuous Deployment**
- Select branches for deployment
- Can choose specific branches or all branches

### 2. Setup Split Test
Navigate to **Project configuration → Build & deploy → Split Testing**
- Choose branches to test
- Set traffic distribution percentages  
- Percentages automatically adjust to total 100%

### 3. Traffic Management
- **Sticky Sessions**: `nf_ab` cookie ensures consistent experience
- **Manual Control**: Set cookie via JavaScript for opt-in testing
- **Real-time Adjustment**: Change percentages anytime

## Analytics Integration

### Expose Branch Information
Inject branch data into site during build:

**Hugo Example:**
```html
<script>
  var testBranch = '{{ getenv "BRANCH" }}';
</script>
```

**React Example:**
```javascript
const testBranch = process.env.BRANCH;
```

### Google Analytics Integration
Track split test data as custom dimensions:

```html
<script>
  ga('send', 'pageview', {
    'Branch': '{{ getenv "BRANCH" }}'
  });
</script>
```

### Segment Integration
Send branch data to multiple analytics platforms:

```html
<script>
  analytics.track('pageview', {
    'Branch': '{{ getenv "BRANCH" }}'
  });
</script>
```

## Snippet Injection Method
Use Netlify's post-processing for flexible analytics:

**Setup:** Project configuration → Build & deploy → Post processing → Snippet injection

**Google Analytics Snippet:**
```html
<script>
  ga('send', 'pageview', {
    'Branch': '{{ BRANCH }}'
  });
</script>
```

**Benefits:**
- Production-only execution
- Framework-agnostic
- Environment variable access
- No build process modification

## Test Management

### Starting Tests
1. Deploy multiple branches
2. Configure traffic split percentages
3. Start test immediately
4. Traffic divides according to settings

### Modifying Tests
- **Add Branches**: Select "Add another branch"
- **Remove Branches**: Use cross button per branch
- **Adjust Traffic**: Real-time percentage changes
- **Single Test**: Only one test active at a time

### Stopping Tests
- Select "Stop test" to end split testing
- All traffic returns to production branch
- Test results remain in analytics

## Best Practices

### Test Design
- **Clear Hypotheses**: Define what you're testing
- **Meaningful Changes**: Ensure branches have significant differences
- **Sufficient Traffic**: Allow adequate sample sizes
- **Test Duration**: Run long enough for statistical significance

### Performance Considerations
- **Static Content**: Best for JAMstack architectures
- **CDN Efficiency**: Leverage Netlify's global CDN
- **Cache Strategy**: Consider cache implications per branch
- **Mobile Performance**: Test across device types

### Analytics Strategy
- **Multiple Platforms**: Use Segment for broad analytics
- **Custom Events**: Track specific user actions
- **Conversion Funnels**: Measure business objectives
- **Statistical Tools**: Use proper A/B testing analysis

### User Experience
- **Consistent Sessions**: Cookie-based user stickiness
- **Progressive Enhancement**: Fallback for disabled JavaScript
- **Loading Performance**: Monitor performance impact
- **Cross-browser Testing**: Ensure compatibility

## Use Cases

### A/B Testing Scenarios
- **Landing Page Optimization**: Different messaging/layouts
- **Conversion Optimization**: Button colors, placement, copy
- **Navigation Testing**: Menu structures, user flows
- **Content Strategy**: Headlines, value propositions

### Feature Rollouts
- **Private Beta**: Limited user access to new features
- **Gradual Rollout**: Percentage-based feature releases
- **Canary Deployments**: Small percentage testing
- **Risk Mitigation**: Easy rollback capability

### Business Intelligence
- **Market Research**: User preference insights
- **Regional Testing**: Geographic performance differences
- **Demographic Analysis**: User segment behaviors
- **Competitive Analysis**: Alternative approaches testing

## Monitoring & Analysis

### Key Metrics
- **Conversion Rates**: Primary success metrics
- **User Engagement**: Time on site, page views
- **Performance Metrics**: Load times, Core Web Vitals
- **Error Rates**: JavaScript errors, failed requests

### Statistical Significance
- **Sample Size**: Ensure adequate user exposure
- **Confidence Intervals**: Typically 95% confidence
- **Test Duration**: Account for weekly/seasonal patterns
- **Early Stopping**: Avoid premature conclusions

### Reporting
- **Dashboard Setup**: Real-time test monitoring
- **Automated Reports**: Scheduled performance summaries
- **Stakeholder Updates**: Business impact communication
- **Post-test Analysis**: Detailed results documentation