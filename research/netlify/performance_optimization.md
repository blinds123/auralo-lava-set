# Netlify Performance Optimization

## Caching Infrastructure

### Default Caching Behavior
- **Static Assets**: Cached for up to 1 year with automatic invalidation
- **Dynamic Responses**: Functions, Edge Functions, proxies not cached by default
- **Atomic Deploy Invalidation**: Cache cleared on new deploys automatically

### Advanced Caching Controls

#### Cache Headers Priority
1. `Netlify-CDN-Cache-Control` (Netlify-specific)
2. `CDN-Cache-Control` (All CDNs) 
3. `Cache-Control` (General)

#### Stale-While-Revalidate
```javascript
'Netlify-CDN-Cache-Control': 'public, max-age=60, stale-while-revalidate=120'
```
- Serves stale content while revalidating in background
- Reduces perceived latency for dynamic content

#### Durable Caching (Functions)
```javascript
'Netlify-CDN-Cache-Control': 'public, durable, max-age=60'
```
- Shares cached responses across edge nodes
- Reduces function invocations significantly
- Better response times for edge cache misses

### Cache Key Variations
Customize cache keys with `Netlify-Vary` header:

```javascript
// By query parameters
'Netlify-Vary': 'query=item_id|page'

// By request headers  
'Netlify-Vary': 'header=Device-Type|App-Version'

// By location
'Netlify-Vary': 'country=us|ca,language=en|fr'

// By cookies
'Netlify-Vary': 'cookie=ab_test|user_type'
```

## Image Optimization

### Netlify Image CDN
Transform images on-demand without build impact:

```html
<!-- Resize and format conversion -->
<img src="/.netlify/images?url=/photo.jpg&w=400&h=300&fm=webp&q=80" />

<!-- Remote images (configure allowlist first) -->
<img src="/.netlify/images?url=https://external.com/image.jpg&w=200" />
```

### Configuration
```toml
[images]
  remote_images = ["https://cdn.example.com/.*"]
```

### Transform Options
- **Size**: `w` (width), `h` (height)
- **Fit**: `contain`, `cover`, `fill`
- **Format**: `webp`, `avif`, `jpg`, `png`, `blurhash`
- **Quality**: `q=1-100` (default 75)
- **Position**: `top`, `bottom`, `left`, `right`, `center`

## Headers for Performance

### Security Headers
```toml
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    X-XSS-Protection = "1; mode=block"
    Referrer-Policy = "strict-origin-when-cross-origin"
```

### Caching Headers
```toml
[[headers]]
  for = "/static/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]  
  for = "/api/*"
  [headers.values]
    Cache-Control = "public, max-age=300, s-maxage=600"
```

## CDN & Edge Optimization

### Global Distribution
- 15+ global edge locations
- Automatic geographic routing
- Reduced latency worldwide

### Edge Functions Performance
- Sub-50ms response times
- Geographic content personalization
- Request/response transformation at edge

### Atomic Deploy Benefits
- Zero-downtime deployments
- Instant rollbacks
- Consistent global state

## Build Optimization

### Build Caching
- Dependency caching between builds
- Node.js, Python, Ruby, Go support
- Custom cache directories configurable

### Framework Optimization
Framework-specific optimizations:
- **Next.js**: Automatic ISR and caching
- **Gatsby**: Build plugin for enhanced caching  
- **Nuxt**: SSR optimizations
- **SvelteKit**: Edge-first deployment

## Monitoring & Analytics

### Core Web Vitals
- Real User Monitoring (RUM)
- Performance insights dashboard
- Core Web Vitals tracking

### Function Performance  
- Invocation duration tracking
- Cold start monitoring
- Error rate analytics

### Cache Hit Rates
- CDN performance metrics
- Cache effectiveness tracking
- Optimization recommendations

## Best Practices

### Asset Optimization
- Enable image format conversion
- Use appropriate image sizes
- Leverage lazy loading

### Code Splitting
- Bundle optimization
- Dynamic imports
- Framework-specific splitting

### Critical Resource Hints
```html
<link rel="preconnect" href="https://api.example.com">
<link rel="dns-prefetch" href="//fonts.googleapis.com">
<link rel="preload" href="/critical.css" as="style">
```

### Compression
- Gzip/Brotli automatic compression
- Asset minification in build process
- Tree shaking unused code

## Performance Testing

### Lighthouse Integration
- Automated performance audits
- CI/CD performance gates
- Historical performance tracking

### Load Testing
- Edge function performance testing
- CDN cache warming strategies
- Geographic performance validation