Title: Overview - OpenAI API

URL Source: https://platform.openai.com/docs/

Markdown Content:
Overview - OpenAI API

===============

[](https://platform.openai.com/docs/overview)

[Docs Docs](https://platform.openai.com/docs)[API reference API](https://platform.openai.com/docs/api-reference/introduction)

Log in[Sign up](https://platform.openai.com/signup)

Search K

Get started

[Overview](https://platform.openai.com/docs/overview)

[Quickstart](https://platform.openai.com/docs/quickstart)

[Models](https://platform.openai.com/docs/models)

[Pricing](https://platform.openai.com/docs/pricing)

[Libraries](https://platform.openai.com/docs/libraries)

Core concepts

[Text generation](https://platform.openai.com/docs/guides/text)

[Images and vision](https://platform.openai.com/docs/guides/images-vision)

[Audio and speech](https://platform.openai.com/docs/guides/audio)

[Structured output](https://platform.openai.com/docs/guides/structured-outputs)

[Function calling](https://platform.openai.com/docs/guides/function-calling)

[Using GPT-5](https://platform.openai.com/docs/guides/latest-model)

Tools

[Using tools](https://platform.openai.com/docs/guides/tools)

[Remote MCP](https://platform.openai.com/docs/guides/tools-remote-mcp)

[Web search](https://platform.openai.com/docs/guides/tools-web-search)

[Code interpreter](https://platform.openai.com/docs/guides/tools-code-interpreter)

File search and retrieval

More tools

Run and scale

[Conversation state](https://platform.openai.com/docs/guides/conversation-state)

[Background mode](https://platform.openai.com/docs/guides/background)

[Streaming](https://platform.openai.com/docs/guides/streaming-responses)

[Webhooks](https://platform.openai.com/docs/guides/webhooks)

[File inputs](https://platform.openai.com/docs/guides/pdf-files)

Prompting

Reasoning

Agents

[Building agents](https://platform.openai.com/docs/guides/agents)

[Voice agents](https://platform.openai.com/docs/guides/voice-agents)

[Agents SDK Python](https://openai.github.io/openai-agents-python)

[Agents SDK TypeScript](https://openai.github.io/openai-agents-js)

Model optimization

[Optimization cycle](https://platform.openai.com/docs/guides/model-optimization)

Evals

Fine-tuning

[Graders](https://platform.openai.com/docs/guides/graders)

Specialized models

[Image generation](https://platform.openai.com/docs/guides/image-generation)

[Text to speech](https://platform.openai.com/docs/guides/text-to-speech)

[Speech to text](https://platform.openai.com/docs/guides/speech-to-text)

[Deep research](https://platform.openai.com/docs/guides/deep-research)

[Embeddings](https://platform.openai.com/docs/guides/embeddings)

[Moderation](https://platform.openai.com/docs/guides/moderation)

Codex

[Codex](https://platform.openai.com/docs/codex/overview)

[Agent internet access](https://platform.openai.com/docs/codex/agent-network)

[Local shell tool](https://platform.openai.com/docs/guides/tools-local-shell)

[Codex CLI](https://github.com/openai/codex)

[Codex Changelog](https://help.openai.com/en/articles/11428266-codex-changelog)

Going live

[Production best practices](https://platform.openai.com/docs/guides/production-best-practices)

Latency optimization

Cost optimization

[Accuracy optimization](https://platform.openai.com/docs/guides/optimizing-llm-accuracy)

Safety

Specialized APIs

Assistants API

Realtime API

[Migrate to Responses API](https://platform.openai.com/docs/guides/migrate-to-responses)

Resources

[Terms and policies](https://openai.com/policies)

[Changelog](https://platform.openai.com/docs/changelog)

[Your data](https://platform.openai.com/docs/guides/your-data)

[Rate limits](https://platform.openai.com/docs/guides/rate-limits)

[Deprecations](https://platform.openai.com/docs/deprecations)

[MCP for deep research](https://platform.openai.com/docs/mcp)

ChatGPT Actions

[Cookbook](https://cookbook.openai.com/)[Forum](https://community.openai.com/categories)

OpenAI developer platform
=========================

[Developer quickstart Make your first API request in minutes. Learn the basics of the OpenAI platform. 5 min](https://platform.openai.com/docs/quickstart)

javascript

```bash
1
2
3
4
5
6
7
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-5",
    "input": "Write a short bedtime story about a unicorn."
  }'
```

```javascript
1
2
3
4
5
6
7
8
9
import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.create({
  model: "gpt-5",
  input: "Write a short bedtime story about a unicorn.",
});

console.log(response.output_text);
```

```python
1
2
3
4
5
6
7
8
9
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="Write a short bedtime story about a unicorn."
)

print(response.output_text)
```

Browse models

[View all](https://platform.openai.com/docs/models)

[GPT-5 The best model for coding and agentic tasks across domains](https://platform.openai.com/docs/models/gpt-5)[GPT-5 mini A faster, cost-efficient version of GPT-5 for well-defined tasks](https://platform.openai.com/docs/models/gpt-5-mini)[GPT-5 nano Fastest, most cost-efficient version of GPT-5](https://platform.openai.com/docs/models/gpt-5-nano)

Start building
--------------

[Read and generate text Use the API to prompt a model and generate text](https://platform.openai.com/docs/guides/text)[Use a model's vision capabilities Allow models to see and analyze images in your application](https://platform.openai.com/docs/guides/images)[Generate images as output Create images with GPT Image 1](https://platform.openai.com/docs/guides/image-generation)[Build apps with audio Analyze, transcribe, and generate audio with API endpoints](https://platform.openai.com/docs/guides/audio)[Build agentic applications Use the API to build agents that use tools and computers](https://platform.openai.com/docs/guides/agents)[Achieve complex tasks with reasoning Use reasoning models to carry out complex tasks](https://platform.openai.com/docs/guides/reasoning)[Get structured data from models Use Structured Outputs to get model responses that adhere to a JSON schema](https://platform.openai.com/docs/guides/structured-outputs)[Tailor to your use case Adjust our models to perform specifically for your use case with fine-tuning, evals, and distillation](https://platform.openai.com/docs/guides/fine-tuning)

[Help center Frequently asked account and billing questions](https://help.openai.com/)[Developer forum Discuss topics with other developers](https://community.openai.com/)[Cookbook Open-source collection of examples and guides](https://cookbook.openai.com/)[Status Check the status of OpenAI services](https://status.openai.com/)
