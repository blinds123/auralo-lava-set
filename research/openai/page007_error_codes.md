# OpenAI Error Codes Documentation

**URL Source:** https://platform.openai.com/docs/guides/error-codes

## API Error Codes Overview

| Code | Overview |
|------|----------|
| 401 - Invalid Authentication | **Cause:** Invalid Authentication **Solution:** Ensure the correct API key and requesting organization are being used. |
| 401 - Incorrect API key provided | **Cause:** The requesting API key is not correct. **Solution:** Ensure the API key used is correct, clear your browser cache, or generate a new one. |
| 401 - You must be a member of an organization to use the API | **Cause:** Your account is not part of an organization. **Solution:** Contact us to get added to a new organization or ask your organization manager to invite you to an organization. |
| 403 - Country, region, or territory not supported | **Cause:** You are accessing the API from an unsupported country, region, or territory. **Solution:** Please see supported countries page for more information. |
| 429 - Rate limit reached for requests | **Cause:** You are sending requests too quickly. **Solution:** Pace your requests. Read the Rate limit guide. |
| 429 - You exceeded your current quota | **Cause:** You have run out of credits or hit your maximum monthly spend. **Solution:** Buy more credits or learn how to increase your limits. |
| 500 - The server had an error while processing your request | **Cause:** Issue on our servers. **Solution:** Retry your request after a brief wait and contact us if the issue persists. Check the status page. |
| 503 - The engine is currently overloaded | **Cause:** Our servers are experiencing high traffic. **Solution:** Please retry your requests after a brief wait. |
| 503 - Slow Down | **Cause:** A sudden increase in your request rate is impacting service reliability. **Solution:** Please reduce your request rate to its original level, maintain consistent rate for 15+ minutes, then gradually increase. |

## Detailed Error Explanations

### 401 - Invalid Authentication

This error indicates invalid authentication credentials. Could happen because:
- Using a revoked API key
- Using a different API key than the one assigned to the requesting organization or project
- Using an API key that doesn't have required permissions for the endpoint

**Resolution steps:**
- Check that you're using the correct API key and organization ID in your request header
- Find your API key and organization ID in your account settings
- Find specific project related keys under General settings by selecting the desired project
- If unsure whether your API key is valid, generate a new one
- Follow best practices guide for API key safety

### 401 - Incorrect API key provided

This error indicates the API key you're using in your request is not correct. Could happen because:
- There is a typo or extra space in your API key
- Using an API key that belongs to a different organization or project
- Using an API key that has been deleted or deactivated
- An old, revoked API key might be cached locally

**Resolution steps:**
- Try clearing your browser's cache and cookies, then try again
- Check that you are using the correct API key in your request header
- If unsure whether your API key is correct, generate a new one
- Replace your old API key in your codebase and follow best practices

### 429 - Rate limit reached for requests

This error indicates you have hit your assigned rate limit. You have submitted too many tokens or requests in a short period. Could happen because:
- Using a loop or script that makes frequent or concurrent requests
- Sharing your API key with other users or applications
- Using a free plan that has a low rate limit
- You have reached the defined limit on your project

**Resolution steps:**
- Pace your requests and avoid making unnecessary or redundant calls
- Implement a backoff mechanism or retry logic that respects the rate limit and response headers
- If sharing your organization with other users, note that limits are applied per organization
- Consider upgrading to a pay-as-you-go plan for higher rate limits
- Reach out to your organization owner to increase rate limits on your project

### 429 - You exceeded your current quota

This error indicates you hit your monthly usage limit for the API, or for prepaid credits customers that you've consumed all your credits. Could happen because:
- Using a high-volume or complex service that consumes a lot of credits or tokens
- Your monthly budget is set too low for your organization's usage
- Your monthly budget is set too low for your project's usage

**Resolution steps:**
- Check your current usage and compare to your account's limits
- If on a free plan, consider upgrading to a paid plan to get higher limits
- Reach out to your organization owner to increase budgets for your project

### 503 - The engine is currently overloaded

This error indicates our servers are experiencing high traffic and are unable to process your request. Could happen because:
- Sudden spike or surge in demand for our services
- Scheduled or unscheduled maintenance or update on our servers
- Unexpected or unavoidable outage or incident on our servers

**Resolution steps:**
- Retry your request after a brief wait using exponential backoff strategy
- Check our status page for any updates or announcements
- Contact us for further assistance if the error persists after reasonable time

### 503 - Slow Down

This error can occur with Pay-As-You-Go models, which are shared across all OpenAI users. It indicates that your traffic has significantly increased, overloading the model and triggering temporary throttling to maintain service stability.

**Resolution steps:**
- Reduce your request rate to its original level
- Keep it stable for at least 15 minutes
- Then gradually ramp it up
- Maintain a consistent traffic pattern to minimize throttling likelihood
- Consider upgrading to the Scale Tier for guaranteed capacity and performance

## Python Library Error Types

| Type | Overview |
|------|----------|
| APIConnectionError | **Cause:** Issue connecting to our services. **Solution:** Check your network settings, proxy configuration, SSL certificates, or firewall rules. |
| APITimeoutError | **Cause:** Request timed out. **Solution:** Retry your request after a brief wait and contact us if the issue persists. |
| AuthenticationError | **Cause:** Your API key or token was invalid, expired, or revoked. **Solution:** Check your API key or token and make sure it is correct and active. |
| BadRequestError | **Cause:** Your request was malformed or missing required parameters. **Solution:** Check the documentation for the specific API method and ensure valid parameters. |
| ConflictError | **Cause:** The resource was updated by another request. **Solution:** Try to update the resource again and ensure no other requests are trying to update it. |
| InternalServerError | **Cause:** Issue on our side. **Solution:** Retry your request after a brief wait and contact us if the issue persists. |
| NotFoundError | **Cause:** Requested resource does not exist. **Solution:** Ensure you are using the correct resource identifier. |
| PermissionDeniedError | **Cause:** You don't have access to the requested resource. **Solution:** Ensure you are using the correct API key, organization ID, and resource ID. |
| RateLimitError | **Cause:** You have hit your assigned rate limit. **Solution:** Pace your requests. Read more in our Rate limit guide. |
| UnprocessableEntityError | **Cause:** Unable to process the request despite the format being correct. **Solution:** Please try the request again. |

## Error Handling Example

```python
import openai
from openai import OpenAI
client = OpenAI()

try:
  #Make your OpenAI API request here
  response = client.chat.completions.create(
    prompt="Hello world",
    model="gpt-4o-mini"
  )
except openai.APIError as e:
  #Handle API error here, e.g. retry or log
  print(f"OpenAI API returned an API Error: {e}")
  pass
except openai.APIConnectionError as e:
  #Handle connection error here
  print(f"Failed to connect to OpenAI API: {e}")
  pass
except openai.RateLimitError as e:
  #Handle rate limit error (we recommend using exponential backoff)
  print(f"OpenAI API request exceeded rate limit: {e}")
  pass
```

## Persistent Error Support

If issues persist, contact support team via chat and provide:
- The model you were using
- The error message and code you received
- The request data and headers you sent
- The timestamp and timezone of your request
- Any other relevant details

You can also post in the Community Forum but be sure to omit sensitive information.