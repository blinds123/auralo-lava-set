# OpenAI Batch API Documentation

**URL Source:** https://platform.openai.com/docs/guides/batch

## Overview

The Batch API allows you to send asynchronous groups of requests with:
- **50% lower costs** compared to synchronous APIs
- **Separate pool of significantly higher rate limits**
- **Clear 24-hour turnaround time**

The service is ideal for processing jobs that don't require immediate responses.

### Best Use Cases
- Running evaluations
- Classifying large datasets
- Embedding content repositories

### Benefits Over Standard Endpoints
1. **Better cost efficiency:** 50% cost discount
2. **Higher rate limits:** Substantially more headroom compared to synchronous APIs
3. **Fast completion times:** Each batch completes within 24 hours (often more quickly)

## Getting Started

### 1. Prepare Your Batch File

Create a `.jsonl` file where each line contains an individual request. Available endpoints:
- `/v1/responses` (Responses API)
- `/v1/chat/completions` (Chat Completions API)
- `/v1/embeddings` (Embeddings API)
- `/v1/completions` (Completions API)

**Example batch file:**
```json
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-3.5-turbo-0125", "messages": [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": "Hello world!"}],"max_tokens": 1000}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-3.5-turbo-0125", "messages": [{"role": "system", "content": "You are an unhelpful assistant."},{"role": "user", "content": "Hello world!"}],"max_tokens": 1000}}
```

### 2. Upload Your Batch Input File

```javascript
import fs from "fs";
import OpenAI from "openai";
const openai = new OpenAI();

const file = await openai.files.create({
  file: fs.createReadStream("batchinput.jsonl"),
  purpose: "batch",
});

console.log(file);
```

### 3. Create the Batch

```javascript
import OpenAI from "openai";
const openai = new OpenAI();

const batch = await openai.batches.create({
  input_file_id: "file-abc123",
  endpoint: "/v1/chat/completions",
  completion_window: "24h"
});

console.log(batch);
```

**Response:**
```json
{
  "id": "batch_abc123",
  "object": "batch",
  "endpoint": "/v1/chat/completions",
  "errors": null,
  "input_file_id": "file-abc123",
  "completion_window": "24h",
  "status": "validating",
  "output_file_id": null,
  "error_file_id": null,
  "created_at": 1714508499,
  "in_progress_at": null,
  "expires_at": 1714536634,
  "completed_at": null,
  "failed_at": null,
  "expired_at": null,
  "request_counts": {
    "total": 0,
    "completed": 0,
    "failed": 0
  },
  "metadata": null
}
```

### 4. Check the Status of a Batch

```javascript
import OpenAI from "openai";
const openai = new OpenAI();

const batch = await openai.batches.retrieve("batch_abc123");
console.log(batch);
```

**Status Types:**

| Status | Description |
|--------|-------------|
| `validating` | The input file is being validated before the batch can begin |
| `failed` | The input file has failed the validation process |
| `in_progress` | The input file was successfully validated and the batch is currently being run |
| `finalizing` | The batch has completed and the results are being prepared |
| `completed` | The batch has been completed and the results are ready |
| `expired` | The batch was not able to be completed within the 24-hour time window |
| `cancelling` | The batch is being cancelled (may take up to 10 minutes) |
| `cancelled` | The batch was cancelled |

### 5. Retrieve the Results

```javascript
import OpenAI from "openai";
const openai = new OpenAI();

const fileResponse = await openai.files.content("file-xyz123");
const fileContents = await fileResponse.text();

console.log(fileContents);
```

**Output format:**
```json
{"id": "batch_req_123", "custom_id": "request-2", "response": {"status_code": 200, "request_id": "req_123", "body": {"id": "chatcmpl-123", "object": "chat.completion", "created": 1711652795, "model": "gpt-3.5-turbo-0125", "choices": [{"index": 0, "message": {"role": "assistant", "content": "Hello."}, "logprobs": null, "finish_reason": "stop"}], "usage": {"prompt_tokens": 22, "completion_tokens": 2, "total_tokens": 24}, "system_fingerprint": "fp_123"}}, "error": null}
```

**Important:** The output line order may not match the input line order. Use the `custom_id` field to map requests in your input to results in your output.

### 6. Cancel a Batch

```javascript
import OpenAI from "openai";
const openai = new OpenAI();

const batch = await openai.batches.cancel("batch_abc123");
console.log(batch);
```

### 7. List All Batches

```javascript
import OpenAI from "openai";
const openai = new OpenAI();

const list = await openai.batches.list();

for await (const batch of list) {
  console.log(batch);
}
```

## Model Availability

The Batch API is widely available across most models, but not all. Please refer to the model reference docs to ensure the model you're using supports the Batch API.

## Rate Limits

Batch API rate limits are separate from existing per-model rate limits:

1. **Per-batch limits:**
   - A single batch may include up to 50,000 requests
   - A batch input file can be up to 200 MB in size
   - `/v1/embeddings` batches are restricted to a maximum of 50,000 embedding inputs across all requests

2. **Enqueued prompt tokens per model:** Each model has a maximum number of enqueued prompt tokens allowed for batch processing. You can find these limits on the Platform Settings page.

**Important:** Using the Batch API will not consume tokens from your standard per-model rate limits, thereby offering you a convenient way to increase the number of requests and processed tokens.

## Batch Expiration

Batches that do not complete in time eventually move to an `expired` state:
- Unfinished requests within that batch are cancelled
- Any responses to completed requests are made available via the batch's output file
- You will be charged for tokens consumed from any completed requests

**Expired requests format:**
```json
{"id": "batch_req_123", "custom_id": "request-3", "response": null, "error": {"code": "batch_expired", "message": "This request could not be executed before the completion window expired."}}
```

The output file will automatically be deleted 30 days after the batch is complete.