# Netlify Deployment Overview

## Atomic Deploys
Netlify enforces atomic deploys - no changes go live until ALL files are uploaded and ready. This prevents broken states during deployment.

### Key Benefits:
- **Consistency**: Site never in inconsistent state during uploads
- **Performance**: Automatic comparison and only uploads changed files
- **Reliability**: No risk of broken assets or missing dependencies
- **CDN Integration**: Immediate activation across global CDN

## Deploy Types

### Production Deploy
- From production branch (usually main/master)
- Auto-publishes if enabled
- Available at main site URL

### Branch Deploy  
- From non-production branches
- URL format: `branch-name--sitename.netlify.app`
- Can enable branch subdomains with Netlify DNS

### Deploy Preview
- From pull/merge requests
- URL format: `deploy-preview-42--sitename.netlify.app`
- Automatic unless disabled

### Permalink
- Every successful deploy gets permanent URL
- Format: `deployid--sitename.netlify.app`
- Content never changes at permalink

## Deploy Summary Features
- File upload count and status
- Headers and redirects validation
- Functions and edge functions deployment count
- Intelligent file deduplication between deploys
- AI-powered failure diagnosis and solutions

## Deploy Contexts
Configure different settings for different deploy types:
- `production`: Main site deployment  
- `deploy-preview`: Pull request previews
- `branch-deploy`: Branch deployments
- `preview-server`: Preview Server environments
- `dev`: Local development with Netlify Dev

## Search Engine Optimization
- Only published production and recent branch deploys are indexable
- Deploy previews and old deploys get `X-Robots-Tag: noindex`
- Custom headers can override for branch deploys