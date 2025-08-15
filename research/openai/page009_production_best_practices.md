# OpenAI Production Best Practices Documentation

**URL Source:** https://platform.openai.com/docs/guides/production-best-practices

## Overview

This guide provides a comprehensive set of best practices to help you transition from prototype to production. Whether you are a seasoned machine learning engineer or a recent enthusiast, this guide should provide you with the tools you need to successfully put the platform to work in a production setting.

## Setting Up Your Organization

### Organization Structure

Once you log in to your OpenAI account, you can find your organization name and ID in your organization settings:
- **Organization name:** The label for your organization, shown in user interfaces
- **Organization ID:** The unique identifier for your organization which can be used in API requests

### Multi-Organization Usage

Users who belong to multiple organizations can pass a header to specify which organization is used for an API request. Usage from these API requests will count against the specified organization's quota. If no header is provided, the default organization will be billed.

### Team Management

You can invite new members to your organization from the Team page. Members can be **readers** or **owners**.

**Readers:**
- Can make API requests
- Can view basic organization information
- Can create, update, and delete resources (like Assistants) in the organization, unless otherwise noted

**Owners:**
- Have all the permissions of readers
- Can modify billing information
- Can manage members within the organization

## Managing Billing Limits

### Initial Setup
To begin using the OpenAI API, enter your billing information. If no billing information is entered, you will still have login access but will be unable to make API requests.

### Usage Limits
Once you've entered your billing information, you will have an approved usage limit of $100 per month, which is set by OpenAI. Your quota limit will automatically increase as your usage increases and you move from one usage tier to another.

### Notifications and Budgets
- Set a notification threshold through the usage limits page
- When the notification threshold is reached, the owners of the organization will receive an email notification
- Set a monthly budget so that, once reached, any subsequent API requests will be rejected
- Note that these limits are best effort, and there may be 5 to 10 minutes of delay between the usage and the limits being enforced

## API Keys

### Security Best Practices
The OpenAI API uses API keys for authentication. This is a relatively straightforward way to control access, but you must be vigilant about securing these keys:

- Avoid exposing the API keys in your code or in public repositories
- Store them in a secure location
- Expose your keys to your application using environment variables or secret management service
- Don't hard-code them in your codebase
- Read more in our Best practices for API key safety

### API Key Tracking
API key usage can be monitored on the Usage page once tracking is enabled:
- If you are using an API key generated prior to Dec 20, 2023 tracking will not be enabled by default
- You can enable tracking going forward on the API key management dashboard
- All API keys generated past Dec 20, 2023 have tracking enabled
- Any previous untracked usage will be displayed as `Untracked` in the dashboard

## Staging Projects

As you scale, you may want to create separate projects for your staging and production environments. You can create these projects in the dashboard, allowing you to:
- Isolate your development and testing work
- Avoid accidentally disrupting your live application
- Limit user access to your production project
- Set custom rate and spend limits per project

## Scaling Your Solution Architecture

When designing your application or service for production that uses our API, consider these key areas:

### Horizontal Scaling
- Scale your application out horizontally to accommodate requests from multiple sources
- Deploy additional servers or containers to distribute the load
- Make sure your architecture is designed to handle multiple nodes
- Have mechanisms in place to balance the load between them

### Vertical Scaling
- Scale your application up vertically by upgrading your server's capabilities
- Make sure your application is designed to take advantage of these additional resources

### Caching
- Store frequently accessed data to improve response times without repeated API calls
- Your application will need to be designed to use cached data whenever possible and invalidate the cache when new information is added
- Options include storing data in a database, filesystem, or in-memory cache

### Load Balancing
- Consider load-balancing techniques to ensure requests are distributed evenly across your available servers
- Could involve using a load balancer in front of your servers or using DNS round-robin
- Balancing the load will help improve performance and reduce bottlenecks

### Managing Rate Limits
When using our API, it's important to understand and plan for rate limits.

## Improving Latencies

### Understanding Latency
Latency is the time it takes for a request to be processed and a response to be returned. The latency of a completion request is mostly influenced by two factors: the model and the number of tokens generated.

**The life cycle of a completion request:**
1. Network: End user to API latency
2. Server: Time to process prompt tokens
3. Server: Time to sample/generate tokens
4. Network: API to end user latency

**Key Insight:** Prompt tokens add very little latency to completion calls. Time to generate completion tokens is much longer, as tokens are generated one at a time. Longer generation lengths will accumulate latency due to generation required for each token.

### Factors Affecting Latency (Most to Least Impactful)

#### 1. Model
Our API offers different models with varying levels of complexity and generality:
- Most capable models, such as `gpt-4`, can generate more complex and diverse completions, but take longer to process
- Models such as `gpt-4o-mini`, can generate faster and cheaper Chat Completions, but may generate results that are less accurate or relevant
- Choose the model that best suits your use case and the trade-off between speed, cost, and quality

#### 2. Number of Completion Tokens
Requesting a large amount of generated tokens can lead to increased latencies:
- **Lower max tokens:** For requests with similar token generation count, those with lower `max_tokens` parameter incur less latency
- **Include stop sequences:** To prevent generating unneeded tokens, add a stop sequence
- **Generate fewer completions:** Lower the values of `n` and `best_of` when possible

#### 3. Streaming
Setting `stream: true` in a request makes the model start returning tokens as soon as they are available, instead of waiting for the full sequence of tokens to be generated. It does not change the time to get all the tokens, but it reduces the time for first token for an application where we want to show partial progress or are going to stop generations.

#### 4. Infrastructure
Our servers are currently located in the US. While we hope to have global redundancy in the future, in the meantime you could consider locating the relevant parts of your infrastructure in the US to minimize the roundtrip time between your servers and the OpenAI servers.

#### 5. Batching
Depending on your use case, batching may help. If you are sending multiple requests to the same endpoint, you can batch the prompts to be sent in the same request. This will reduce the number of requests you need to make. The prompt parameter can hold up to 20 unique prompts.

## Managing Costs

### Monitoring Costs
To monitor your costs, you can:
- Set a notification threshold in your account to receive an email alert once you pass a certain usage threshold
- Set a monthly budget
- Be mindful of the potential for a monthly budget to cause disruptions to your application/users
- Use the usage tracking dashboard to monitor your token usage during the current and past billing cycles

### Cost Reduction Framework
One useful framework for thinking about reducing costs is to consider costs as a function of the number of tokens and the cost per token. Two potential avenues for reducing costs:

1. **Reduce the cost per token** by switching to smaller models for some tasks
2. **Reduce the number of tokens required** by:
   - Using shorter prompts
   - Fine-tuning models
   - Caching common user queries so that they don't need to be processed repeatedly

### Tools for Cost Estimation
- Experiment with our interactive tokenizer tool to help you estimate costs
- The API and playground also returns token counts as part of the response
- Once you've got things working with our most capable model, you can see if the other models can produce the same results with lower latency and costs

## MLOps Strategy

As you move your prototype into production, you may want to consider developing an MLOps strategy. MLOps (machine learning operations) refers to the process of managing the end-to-end life cycle of your machine learning models.

### Key Areas to Consider

**Data and model management:** Managing the data used to train or fine-tune your model and tracking versions and changes.

**Model monitoring:** Tracking your model's performance over time and detecting any potential issues or degradation.

**Model retraining:** Ensuring your model stays up to date with changes in data or evolving requirements and retraining or fine-tuning it as needed.

**Model deployment:** Automating the process of deploying your model and related artifacts into production.

## Security and Compliance

As you move your prototype into production, you will need to assess and address any security and compliance requirements that may apply to your application.

### Key Areas to Consider
- Data storage
- Data transmission
- Data retention
- Data privacy protections (encryption or anonymization where possible)
- Secure coding best practices (input sanitization and proper error handling)

### Resources
- Our security practices and trust and compliance portal provide our most comprehensive and up-to-date documentation
- Privacy Policy and Terms of Use
- Safety best practices to ensure your application is safe and successful

## Business Considerations

As projects using AI move from prototype to production, it is important to consider how to build a great product with AI and how that ties back to your core business.