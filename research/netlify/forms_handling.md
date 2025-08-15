# Netlify Forms

## Overview
Serverless form handling without extra API calls or JavaScript. Built-in form detection parses HTML at deploy time automatically.

## Setup Process

### 1. Enable Form Detection
- Navigate to **Forms** section in Netlify UI
- Select **Enable form detection**
- Applies to next site deploy automatically

### 2. HTML Form Configuration
Add `data-netlify="true"` or `netlify` attribute to form tag:

```html
<form name="contact" method="POST" data-netlify="true">
  <input type="text" name="name" required />
  <input type="email" name="email" required />
  <textarea name="message"></textarea>
  <button type="submit">Send</button>
</form>
```

## Framework-Specific Implementation

### JavaScript/SSR Frameworks
For Next.js, Gatsby, Nuxt, etc., create hidden HTML form with matching fields:
- Include all input names from JS form
- Add `data-netlify="true"` attribute
- Include `<input type="hidden" name="form-name" value="form_name" />`

### AJAX Submission
```javascript
const handleSubmit = event => {
  event.preventDefault();
  const formData = new FormData(event.target);
  
  fetch("/", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams(formData).toString()
  })
  .then(() => console.log("Form successfully submitted"))
  .catch(error => alert(error));
};
```

## Advanced Features

### File Uploads
- Add `<input type="file" name="file" />` to forms
- Optional `enctype="multipart/form-data"` attribute
- **Limits**: 8 MB max size, 30s timeout, one file per field
- **Security**: Use VGS integration for PII files

### Custom Success Pages
Add `action="/success"` attribute to redirect after submission

### Spam Protection
- Built-in spam filtering
- reCAPTCHA integration support
- Honeypot fields for bot detection

## Notifications Setup
Configure notifications to receive form submissions:
- **Email notifications**: Send to team members
- **Webhook notifications**: POST to external services
- **Slack integration**: Direct channel notifications

## Form Management
- **Submissions Dashboard**: View all form entries
- **Export Data**: Download submissions as CSV
- **Spam Management**: Review and manage spam
- **Usage Tracking**: Monitor submission volume

## Best Practices
- **Form Names**: Use unique names for multiple forms
- **Validation**: Implement client-side validation
- **Security**: Never expose sensitive data in forms
- **Testing**: Test forms in Deploy Previews
- **Performance**: Minimize form fields for better UX

## Limitations & Considerations
- **JSON Support**: Forms don't support JSON data
- **File Limits**: 8 MB maximum file size
- **Processing Time**: 30-second timeout for uploads
- **Pricing**: Based on submission volume and storage