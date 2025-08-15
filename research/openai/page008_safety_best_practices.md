# OpenAI Safety Best Practices Documentation

**URL Source:** https://platform.openai.com/docs/guides/safety-best-practices

## Overview

Implement safety measures like moderation and human oversight when deploying OpenAI API applications in production.

## Use Our Free Moderation API

OpenAI's Moderation API is free-to-use and can help reduce the frequency of unsafe content in your completions. Alternatively, you may wish to develop your own content filtration system tailored to your use case.

## Adversarial Testing

We recommend "red-teaming" your application to ensure it's robust to adversarial input. Test your product over a wide range of inputs and user behaviors, both a representative set and those reflective of someone trying to 'break' your application.

**Key testing scenarios:**
- Does it wander off topic?
- Can someone easily redirect the feature via prompt injections, e.g. "ignore the previous instructions and do this instead"?

## Human in the Loop (HITL)

Wherever possible, we recommend having a human review outputs before they are used in practice. This is especially critical in:
- High-stakes domains
- Code generation

Humans should be aware of the limitations of the system, and have access to any information needed to verify the outputs (for example, if the application summarizes notes, a human should have easy access to the original notes to refer back).

## Prompt Engineering

"Prompt engineering" can help constrain the topic and tone of output text. This reduces the chance of producing undesired content, even if a user tries to produce it. 

**Techniques:**
- Providing additional context to the model
- Giving a few high-quality examples of desired behavior prior to the new input
- Makes it easier to steer model outputs in desired directions

## "Know Your Customer" (KYC)

Users should generally need to register and log-in to access your service. 

**Security measures:**
- Linking service to existing account (Gmail, LinkedIn, Facebook log-in) may help, though may not be appropriate for all use-cases
- Requiring a credit card or ID card reduces risk further

## Constrain User Input and Limit Output Tokens

**Input constraints:**
- Limiting the amount of text a user can input into the prompt helps avoid prompt injection
- Narrowing the ranges of inputs, especially drawn from trusted sources, reduces the extent of misuse possible
- Allowing user inputs through validated dropdown fields (e.g., a list of movies on Wikipedia) can be more secure than allowing open-ended text inputs

**Output constraints:**
- Limiting the number of output tokens helps reduce the chance of misuse
- Returning outputs from a validated set of materials on the backend, where possible, can be safer than returning novel generated content
- For instance, routing a customer query to the best-matching existing customer support article, rather than attempting to answer the query from-scratch

## Allow Users to Report Issues

Users should generally have an easily-available method for reporting improper functionality or other concerns about application behavior:
- Listed email address
- Ticket submission method
- Should be monitored by a human and responded to as appropriate

## Understand and Communicate Limitations

From hallucinating inaccurate information, to offensive outputs, to bias, and much more, language models may not be suitable for every use case without significant modifications. 

**Consider:**
- Whether the model is fit for your purpose
- Evaluate the performance of the API on a wide range of potential inputs to identify cases where the API's performance might drop
- Consider your customer base and the range of inputs that they will be using
- Ensure their expectations are calibrated appropriately

## Implement Safety Identifiers

Sending safety identifiers in your requests can be a useful tool to help OpenAI monitor and detect abuse. This allows OpenAI to provide your team with more actionable feedback in the event that we detect any policy violations in your application.

A safety identifier should be a string that uniquely identifies each user. Hash the username or email address in order to avoid sending us any identifying information. If you offer a preview of your product to non-logged in users, you can send a session ID instead.

### Example: Providing a Safety Identifier

**Python:**
```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": "This is a test"}
  ],
  max_tokens=5,
  safety_identifier="user_123456"
)
```

**cURL:**
```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
  "model": "gpt-4o-mini",
  "messages": [
    {"role": "user", "content": "This is a test"}
  ],
  "max_tokens": 5,
  "safety_identifier": "user123456"
}'
```

## Security Contact

Safety and security are very important to us at OpenAI.

If you notice any safety or security issues while developing with the API or anything else related to OpenAI, please submit it through our [Coordinated Vulnerability Disclosure Program](https://openai.com/security/disclosure/).