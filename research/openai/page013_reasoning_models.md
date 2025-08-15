# OpenAI Reasoning Models Documentation

**URL Source:** https://platform.openai.com/docs/guides/reasoning

## Overview

**Reasoning models** like GPT-5 are LLMs trained with reinforcement learning to perform reasoning. Reasoning models "think before they answer", producing a long internal chain of thought before responding to the user.

### Key Capabilities
- Excel in complex problem solving
- Advanced coding capabilities  
- Scientific reasoning
- Multi-step planning for agentic workflows
- Best models for Codex CLI (lightweight coding agent)

### Available Models
- **GPT-5**: Larger model, slower and more expensive but often generates better responses for complex tasks and broad domains
- **gpt-5-mini**: Smaller, faster model, less expensive per token
- **gpt-5-nano**: Smallest, fastest version

## Getting Started with Reasoning

Reasoning models can be used through the Responses API:

```python
from openai import OpenAI

client = OpenAI()

prompt = """
Write a bash script that takes a matrix represented as a string with 
format '[1,2],[3,4],[5,6]' and prints the transpose in the same format.
"""

response = client.responses.create(
    model="gpt-5",
    reasoning={"effort": "medium"},
    input=[
        {
            "role": "user", 
            "content": prompt
        }
    ]
)

print(response.output_text)
```

### Reasoning Effort Parameter
The `reasoning.effort` parameter guides the model on how many reasoning tokens to generate:
- **low**: Favors speed and economical token usage
- **medium**: Balance between speed and reasoning accuracy (default)
- **high**: Favors more complete reasoning

## How Reasoning Works

Reasoning models introduce **reasoning tokens** in addition to input and output tokens:

1. Models use reasoning tokens to "think" - breaking down the prompt and considering multiple approaches
2. After generating reasoning tokens, the model produces an answer as visible completion tokens
3. Reasoning tokens are discarded from context but retained for billing

### Context Window Management
- Reasoning tokens occupy space in the model's context window
- Reasoning tokens are billed as output tokens
- Models may generate hundreds to tens of thousands of reasoning tokens depending on problem complexity
- Exact number visible in response `usage.output_tokens_details.reasoning_tokens`

### Cost Control
- Use `max_output_tokens` parameter to limit total tokens (reasoning + final output)
- If tokens reach limit, you get `status: "incomplete"` with `incomplete_details.reason: "max_output_tokens"`
- Recommend reserving at least 25,000 tokens for reasoning and outputs when experimenting

### Example Usage Object
```json
{
    "usage": {
        "input_tokens": 75,
        "input_tokens_details": {
            "cached_tokens": 0
        },
        "output_tokens": 1186,
        "output_tokens_details": {
            "reasoning_tokens": 1024
        },
        "total_tokens": 1261
    }
}
```

## Handling Incomplete Responses

```python
response = client.responses.create(
    model="gpt-5",
    reasoning={"effort": "medium"},
    input=[{"role": "user", "content": prompt}],
    max_output_tokens=300,
)

if response.status == "incomplete" and response.incomplete_details.reason == "max_output_tokens":
    print("Ran out of tokens")
    if response.output_text:
        print("Partial output:", response.output_text)
    else: 
        print("Ran out of tokens during reasoning")
```

## Function Calling with Reasoning Models

When doing function calling with reasoning models:
- Pass back any reasoning items returned with the last function call
- Include reasoning items, function call items, and function call output items since the last user message
- Use `previous_response_id` parameter or manually pass all output items from past response
- Ensures model continues reasoning process token-efficiently

### Encrypted Reasoning Items
For stateless mode or zero data retention:
- Must retain reasoning items across conversation turns
- Include `reasoning.encrypted_content` in the `include` parameter
- Reasoning items will have `encrypted_content` property for future turns

```bash
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "o4-mini",
    "reasoning": {"effort": "medium"},
    "input": "What is the weather like today?",
    "tools": [ ... function config here ... ],
    "include": [ "reasoning.encrypted_content" ]
  }'
```

## Reasoning Summaries

While raw reasoning tokens aren't exposed, you can view summaries of the model's reasoning:

```python
response = client.responses.create(
    model="gpt-5",
    input="What is the capital of France?",
    reasoning={
        "effort": "low",
        "summary": "auto"  # Most detailed summarizer available
    }
)
```

### Summary Settings
- **auto**: Most detailed summarizer available for the model
- **detailed**: Comprehensive reasoning summary (available for most models)
- **concise**: Brief reasoning summary (available for some models like computer use model)

### Example Summary Output
```json
[
    {
        "id": "rs_6876cf02e0bc8192b74af0fb64b715ff06fa2fcced15a5ac",
        "type": "reasoning",
        "summary": [
            {
                "type": "summary_text",
                "text": "**Answering a simple question**\n\nI'm looking at a straightforward question: the capital of France is Paris. It's a well-known fact, and I want to keep it brief and to the point. Paris is known for its history, art, and culture, so it might be nice to add just a hint of that charm. But mostly, I'll aim to focus on delivering a clear and direct answer, ensuring the user gets what they're looking for without any extra fluff."
            }
        ]
    }
]
```

## Prompting Advice

Reasoning models differ from GPT models in prompting approach:

### Reasoning Models (like a senior co-worker)
- Give them a goal to achieve
- Trust them to work out the details
- Better results with only high-level guidance

### GPT Models (like a junior coworker)
- Perform best with explicit instructions
- Need very precise instructions to create specific output

## Use Case Examples

### Coding (Refactoring)
```python
prompt = """
Instructions:
- Given the React component below, change it so that nonfiction books have red text
- Return only the code in your reply
- Do not include any additional formatting, such as markdown code blocks
- For formatting, use four space tabs, and do not allow any lines of code to exceed 80 columns

const books = [
  { title: 'Dune', category: 'fiction', id: 1 },
  { title: 'Frankenstein', category: 'fiction', id: 2 },
  { title: 'Moneyball', category: 'nonfiction', id: 3 },
];

export default function BookList() {
  const listItems = books.map(book =>
    <li>
      {book.title}
    </li>
  );

  return (
    <ul>{listItems}</ul>
  );
}
"""

response = client.responses.create(
    model="gpt-5",
    input=[{"role": "user", "content": prompt}]
)
```

### Coding (Planning)
```python
prompt = """
I want to build a Python app that takes user questions and looks 
them up in a database where they are mapped to answers. If there 
is close match, it retrieves the matched answer. If there isn't, 
it asks the user to provide an answer and stores the 
question/answer pair in the database. Make a plan for the directory 
structure you'll need, then return each file in full. Only supply 
your reasoning at the beginning and end, not throughout the code.
"""

response = client.responses.create(
    model="gpt-5",
    input=[{"role": "user", "content": prompt}]
)
```

### STEM Research
```python
prompt = """
What are three compounds we should consider investigating to 
advance research into new antibiotics? Why should we consider 
them?
"""

response = client.responses.create(
    model="gpt-5",
    input=[{"role": "user", "content": prompt}]
)
```

## Best Practices

1. **Reserve adequate token space**: At least 25,000 tokens for reasoning and outputs
2. **Use appropriate effort level**: Start with "medium", adjust based on task complexity
3. **Handle incomplete responses**: Check response status and incomplete_details
4. **Function calling**: Always pass back reasoning items between function calls
5. **High-level guidance**: Give reasoning models goals rather than step-by-step instructions
6. **Monitor reasoning token usage**: Check `output_tokens_details.reasoning_tokens` in usage object