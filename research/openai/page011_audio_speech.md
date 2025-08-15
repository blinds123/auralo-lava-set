# OpenAI Audio and Speech Documentation

**URL Source:** https://platform.openai.com/docs/guides/audio

## Overview

The OpenAI API provides a range of audio capabilities. LLMs can process audio by using sound as input, creating sound as output, or both. OpenAI has several API endpoints that help you build audio applications or voice agents.

## Audio Use Cases Tour

### Voice Agents
Voice agents understand audio to handle tasks and respond back in natural language. There are two main ways to approach voice agents:

1. **Speech-to-Speech Models with Realtime API** - Lower latency and more natural
2. **Chained Approach** - Speech-to-text → text language model → text-to-speech
   - More reliable way to extend a text-based agent into a voice agent
   - If using the Agents SDK, you can extend existing agents with voice capabilities using the chained approach

### Streaming Audio
Process audio in real time to build voice agents and other low-latency applications, including transcription use cases. You can stream audio in and out of a model with the Realtime API. Advanced speech models provide:
- Automatic speech recognition for improved accuracy
- Low-latency interactions
- Multilingual support

### Text to Speech
For turning text into speech, use the Audio API `audio/speech` endpoint. Compatible models:
- `gpt-4o-mini-tts` - Can ask the model to speak a certain way or with a certain tone of voice
- `tts-1`
- `tts-1-hd`

### Speech to Text
For speech to text, use the Audio API `audio/transcriptions` endpoint. Compatible models:
- `gpt-4o-transcribe`
- `gpt-4o-mini-transcribe`
- `whisper-1`

With streaming, you can continuously pass in audio and get a continuous stream of text back.

## Choosing the Right API

Multiple APIs are available for transcribing or generating audio:

| API | Supported modalities | Streaming support |
|-----|---------------------|------------------|
| [Realtime API](https://platform.openai.com/docs/api-reference/realtime) | Audio and text inputs and outputs | Audio streaming in and out |
| [Chat Completions API](https://platform.openai.com/docs/api-reference/chat) | Audio and text inputs and outputs | Audio streaming out |
| [Transcription API](https://platform.openai.com/docs/api-reference/audio) | Audio inputs | Audio streaming out |
| [Speech API](https://platform.openai.com/docs/api-reference/audio) | Text inputs and audio outputs | Audio streaming out |

### General Use vs. Specialized APIs

**General Use APIs:**
- Realtime and Chat Completions APIs use our latest models' native audio understanding and generation capabilities
- Can combine with other features like function calling
- Can be used for a wide range of use cases
- You can select the model you want to use

**Specialized APIs:**
- Transcription, Translation and Speech APIs are specialized to work with specific models
- Only meant for one purpose

### Talking with a Model vs. Controlling the Script

**Conversational Interactions:**
- Use the Realtime or Chat Completions API for design conversational interactions where the model thinks and responds in speech
- You won't know exactly what the model will say ahead of time
- The conversation will feel natural

**More Control and Predictability:**
- Use the Speech-to-text / LLM / Text-to-speech pattern
- You know exactly what the model will say and can control the response
- Note: This method will have added latency

### Recommendations

- **Real-time interactions or transcription**: Use the Realtime API
- **Voice agent or audio-based application requiring features like function calling**: Use the Chat Completions API (if realtime is not a requirement)
- **Use cases with one specific purpose**: Use the Transcription, Translation, or Speech APIs

## Adding Audio to Existing Applications

Models such as GPT-4o or GPT-4o mini are natively multimodal, meaning they can understand and generate multiple modalities as input and output.

If you already have a text-based LLM application with the Chat Completions endpoint, you can add audio capabilities by including `audio` in the `modalities` array and using an audio model, like `gpt-4o-audio-preview`.

### Audio Output from Model

```javascript
import { writeFileSync } from "node:fs";
import OpenAI from "openai";

const openai = new OpenAI();

// Generate an audio response to the given prompt
const response = await openai.chat.completions.create({
  model: "gpt-4o-audio-preview",
  modalities: ["text", "audio"],
  audio: { voice: "alloy", format: "wav" },
  messages: [
    {
      role: "user",
      content: "Is a golden retriever a good family dog?"
    }
  ],
  store: true,
});

// Inspect returned data
console.log(response.choices[0]);

// Write audio data to a file
writeFileSync(
  "dog.wav",
  Buffer.from(response.choices[0].message.audio.data, 'base64'),
  { encoding: "utf-8" }
);
```