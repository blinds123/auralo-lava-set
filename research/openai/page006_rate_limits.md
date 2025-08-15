# OpenAI Rate Limits Documentation

**URL Source:** https://platform.openai.com/docs/guides/rate-limits

## Overview

Rate limits are restrictions that the OpenAI API imposes on the number of times a user or client can access services within a specified period of time.

## Why Do We Have Rate Limits?

Rate limits are in place for several reasons:

- **Protection against abuse or misuse** - Prevents malicious actors from flooding the API with requests
- **Fair access for everyone** - Ensures one person/organization can't bog down the API for others
- **Infrastructure management** - Helps OpenAI manage aggregate load on infrastructure

## How Rate Limits Work

Rate limits are measured in five ways:
- **RPM** (requests per minute)
- **RPD** (requests per day) 
- **TPM** (tokens per minute)
- **TPD** (tokens per day)
- **IPM** (images per minute)

Rate limits can be hit across any of these options depending on what occurs first.

### Important Notes
- Rate limits are defined at the organization level and project level, not user level
- Rate limits vary by the model being used
- For long context models like GPT-4.1, there is a separate rate limit for long context requests
- Limits are also placed on total monthly spend (usage limits)
- Some model families have shared rate limits

### Batch API Queue Limits
Calculated based on total number of input tokens queued for a given model. Tokens from pending batch jobs count against your queue limit.

## Usage Tiers

As your spend increases, you automatically graduate to the next usage tier with increased rate limits:

| Tier | Qualification | Usage limits |
|------|--------------|-------------|
| Free | User must be in allowed geography | $100 / month |
| Tier 1 | $5 paid | $100 / month |
| Tier 2 | $50 paid and 7+ days since first payment | $500 / month |
| Tier 3 | $100 paid and 7+ days since first payment | $1,000 / month |
| Tier 4 | $250 paid and 14+ days since first payment | $5,000 / month |
| Tier 5 | $1,000 paid and 30+ days since first payment | $200,000 / month |

## Rate Limit Headers

HTTP response headers provide information about your rate limits:

| Field | Sample Value | Description |
|-------|-------------|-------------|
| x-ratelimit-limit-requests | 60 | Maximum requests permitted before exhausting rate limit |
| x-ratelimit-limit-tokens | 150000 | Maximum tokens permitted before exhausting rate limit |
| x-ratelimit-remaining-requests | 59 | Remaining requests before exhausting rate limit |
| x-ratelimit-remaining-tokens | 149984 | Remaining tokens before exhausting rate limit |
| x-ratelimit-reset-requests | 1s | Time until rate limit (requests) resets |
| x-ratelimit-reset-tokens | 6m0s | Time until rate limit (tokens) resets |

## Fine-tuning Rate Limits

Fine-tuning rate limits can be found in the dashboard and retrieved via API:

```bash
curl https://api.openai.com/v1/fine_tuning/model_limits \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

## Error Mitigation

### Retrying with Exponential Backoff

Automatically retry requests with random exponential backoff when hitting rate limits.

#### Example 1: Using Tenacity Library

```python
from openai import OpenAI
client = OpenAI()

from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def completion_with_backoff(**kwargs):
    return client.completions.create(**kwargs)

completion_with_backoff(model="gpt-4o-mini", prompt="Once upon a time,")
```

#### Example 2: Using Backoff Library

```python
import backoff 
import openai
from openai import OpenAI
client = OpenAI()

@backoff.on_exception(backoff.expo, openai.RateLimitError)
def completions_with_backoff(**kwargs):
    return client.completions.create(**kwargs)

completions_with_backoff(model="gpt-4o-mini", prompt="Once upon a time,")
```

#### Example 3: Manual Backoff Implementation

```python
import random
import time
import openai
from openai import OpenAI
client = OpenAI()

def retry_with_exponential_backoff(
    func,
    initial_delay: float = 1,
    exponential_base: float = 2,
    jitter: bool = True,
    max_retries: int = 10,
    errors: tuple = (openai.RateLimitError,),
):
    """Retry a function with exponential backoff."""

    def wrapper(*args, **kwargs):
        num_retries = 0
        delay = initial_delay

        while True:
            try:
                return func(*args, **kwargs)

            except errors as e:
                num_retries += 1

                if num_retries > max_retries:
                    raise Exception(
                        f"Maximum number of retries ({max_retries}) exceeded."
                    )

                delay *= exponential_base * (1 + jitter * random.random())
                time.sleep(delay)

            except Exception as e:
                raise e

    return wrapper

@retry_with_exponential_backoff
def completions_with_backoff(**kwargs):
    return client.completions.create(**kwargs)
```

## Other Mitigation Strategies

### Reduce max_tokens
Set `max_tokens` as close to your expected response size as possible since rate limit is calculated as the maximum of `max_tokens` and estimated tokens.

### Batching Requests
- Use Batch API for non-immediate responses
- For synchronous responses, batch multiple tasks into each request to process more tokens per minute

### Additional Best Practices
- Exercise caution with programmatic access and bulk processing features
- Set usage limits for individual users within specified time frames
- Consider hard caps or manual review processes for users exceeding limits