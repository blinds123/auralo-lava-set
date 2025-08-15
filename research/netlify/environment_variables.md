# Netlify Environment Variables

## Overview
Configure site builds and functionality with environment variables that support different scopes, deploy contexts, and security levels.

## Variable Types

### Site Environment Variables
- Specific to individual sites
- Override shared variables with same name
- Full scope and context control

### Shared Environment Variables  
- Available to all sites in team
- Team Owners only can read/edit
- Useful for common API keys, configurations

## Scopes & Availability

### Builds Scope
- Site builds and framework builds
- Configure build tools and frameworks
- Available during build process

### Functions Scope  
- Serverless Functions, Edge Functions
- On-demand Builders
- Runtime environment access

### Runtime Scope
- Forms (reCAPTCHA keys)  
- Signed proxy redirects
- Browser-side execution

### Post Processing Scope
- Snippet injection
- Analytics script configuration
- Build-time HTML processing

## Deploy Context Values
Set different values per deploy context:
- **Production**: Main site deployment
- **Deploy Previews**: Pull request previews  
- **Branch Deploys**: Non-production branches
- **Preview Server**: Preview environments
- **Local Development**: Netlify CLI usage
- **Branch-Specific**: Target individual branches

## Security Features

### Secrets Controller
- Mark variables as "Contains secret values"
- Additional access restrictions
- Enhanced security for sensitive data
- Audit logging for secret access

### Sensitive Variable Policy
- Control access for public repositories
- Prevent untrusted deploys from accessing secrets
- Manual approval workflow for contributors

## Configuration Methods

### Netlify UI/CLI/API (Recommended)
- Stored securely on Netlify
- Support for all scopes and contexts
- Team audit log tracking
- Secrets Controller compatibility

### netlify.toml File
- Stored in repository
- Limited to build scope
- Context-specific values supported
- **Warning**: Avoid secrets in public repos

## Best Practices

### Security
- Use UI/CLI/API for sensitive values
- Enable Secrets Controller for critical data
- Review sensitive variable policies
- Regular audit of variable access

### Organization
- Use descriptive variable names
- Group related variables logically
- Document variable purposes
- Clean up unused variables

### Performance
- Scope variables appropriately
- Avoid unnecessary variable exposure
- Use shared variables for common configs
- Monitor variable limits (255 char keys, 5000 char values)

## Integration Examples

### Build Configuration
```bash
# Build environment
NODE_ENV=production
BUILD_COMMAND=npm run build:prod
HUGO_VERSION=0.121.0
```

### API Integration
```javascript
// Functions runtime
const API_KEY = process.env.API_KEY;
const DATABASE_URL = process.env.DATABASE_URL;
```

### Framework Configuration
```javascript
// Next.js
NEXT_PUBLIC_GA_ID=process.env.NEXT_PUBLIC_GA_ID
NEXTAUTH_SECRET=process.env.NEXTAUTH_SECRET
```

## Limitations & Considerations
- **Key Format**: Alphanumeric + underscore, letter first
- **Character Limits**: 255 chars (key), 5000 chars (value)
- **Reserved Names**: Netlify read-only variables protected
- **Context Precedence**: More specific contexts override general
- **Function Limits**: AWS Lambda environment property limits apply