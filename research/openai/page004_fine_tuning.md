# OpenAI Model Optimization and Fine-tuning Documentation

**URL Source:** https://platform.openai.com/docs/guides/fine-tuning

## Model Optimization Workflow

Optimizing model output requires a combination of **evals**, **prompt engineering**, and **fine-tuning**, creating a flywheel of feedback that leads to better prompts and better training data for fine-tuning. The optimization process:

1. Write evals that measure model output, establishing a baseline for performance and accuracy.
2. Prompt the model for output, providing relevant context data and instructions.
3. For some use cases, fine-tune a model for a specific task.
4. Run evals using test data that is representative of real world inputs.
5. Tweak your prompt or fine-tuning dataset based on eval feedback.
6. Repeat the loop continuously to improve your model results.

## Build Evals

In the OpenAI platform, you can build and run evals either via API or in the dashboard. You might consider writing evals before you start writing prompts, taking an approach akin to behavior-driven development (BDD).

Run your evals against test inputs like you expect to see in production. Using available graders, measure the results of a prompt against your test data set.

## Write Effective Prompts

With evals in place, you can effectively iterate on prompts. The prompt engineering process may be all you need to get great results. Best practices:

- **Include relevant context** - in your instructions, include text or image content that the model will need to generate a response from outside its training data.
- **Provide clear instructions** - your prompt should contain clear goals about what kind of output you want. GPT models like `gpt-4.1` are great at following very explicit instructions, while reasoning models like `o4-mini` tend to do better with high level guidance on outcomes.
- **Provide example outputs** - give the model a few examples of correct output for a given prompt (few-shot learning).

## Fine-tune a Model

OpenAI models are already pre-trained to perform across a broad range of subjects and tasks. Fine-tuning lets you take an OpenAI base model, provide the kinds of inputs and outputs you expect in your application, and get a model that excels in the tasks you'll use it for.

Fine-tuning benefits over prompting alone:
- You can provide more example inputs and outputs than could fit within the context window of a single request
- You can use shorter prompts with fewer examples and context data, which saves on token costs at scale and can be lower latency
- You can train on proprietary or sensitive data without having to include it via examples in every request
- You can train a smaller, cheaper, faster model to excel at a particular task where a larger model is not cost-effective

## Fine-tuning Methods

| Method | How it works | Best for | Use with |
|--------|-------------|----------|----------|
| [Supervised fine-tuning (SFT)](https://platform.openai.com/docs/guides/supervised-fine-tuning) | Provide examples of correct responses to prompts to guide the model's behavior. Often uses human-generated "ground truth" responses. | • Classification<br>• Nuanced translation<br>• Generating content in a specific format<br>• Correcting instruction-following failures | `gpt-4.1-2025-04-14`<br>`gpt-4.1-mini-2025-04-14`<br>`gpt-4.1-nano-2025-04-14` |
| [Vision fine-tuning](https://platform.openai.com/docs/guides/vision-fine-tuning) | Provide image inputs for supervised fine-tuning to improve the model's understanding of image inputs. | • Image classification<br>• Correcting failures in instruction following for complex prompts | `gpt-4o-2024-08-06` |
| [Direct preference optimization (DPO)](https://platform.openai.com/docs/guides/direct-preference-optimization) | Provide both a correct and incorrect example response for a prompt. Indicate the correct response to help the model perform better. | • Summarizing text, focusing on the right things<br>• Generating chat messages with the right tone and style | `gpt-4.1-2025-04-14`<br>`gpt-4.1-mini-2025-04-14`<br>`gpt-4.1-nano-2025-04-14` |
| [Reinforcement fine-tuning (RFT)](https://platform.openai.com/docs/guides/reinforcement-fine-tuning) | Generate a response for a prompt, provide an expert grade for the result, and reinforce the model's chain-of-thought for higher-scored responses. **Reasoning models only**. | • Complex domain-specific tasks that require advanced reasoning<br>• Medical diagnoses based on history and diagnostic guidelines<br>• Determining relevant passages from legal case law | `o4-mini-2025-04-16` |

## How Fine-tuning Works

The general shape of the fine-tuning process:

1. Collect a dataset of examples to use as training data
2. Upload that dataset to OpenAI, formatted in JSONL
3. Create a fine-tuning job using one of the methods above, depending on your goals—this begins the fine-tuning training process
4. In the case of RFT, you'll also define a grader to score the model's behavior
5. Evaluate the results

You can create fine-tuned models either in the dashboard or with the API.

## Learn from Experts

Model optimization is a complex topic, and sometimes more art than science. The OpenAI team provides educational videos on:
- Cost/accuracy/latency optimization
- Distillation techniques
- Optimizing LLM Performance