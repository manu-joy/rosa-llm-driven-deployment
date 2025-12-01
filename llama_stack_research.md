# Llama Stack Research: Architecture, Agents, and Platform Integration

## 1. Executive Summary

**Llama Stack** is Meta's open-source, standardized interface for building generative AI applications. It acts as a modular abstraction layer (like an operating system for AI) that sits between your application code and the underlying AI infrastructure (models, vector DBs, safety tools).

**Key Findings:**
- **Purpose**: To provide a consistent, portable API for building AI apps that can run anywhere (local, cloud, on-premise) without code changes.
- **Agent Orchestration**: Built-in "Agents API" manages memory, tool calling, and multi-step reasoning.
- **OpenShift Integration**: Fully supported via the **Llama Stack Kubernetes Operator** and integrates with **Red Hat OpenShift AI (RHOAI)**.
- **Java Support**: No native Java SDK yet. Java agents must interact via **REST APIs** or by generating a client from the OpenAPI/gRPC specifications.

---

## 2. General Architecture & Purpose

Llama Stack is designed around the concept of **"Providers"** and **"APIs"**.

### The "Stack" Layers
1.  **Application Layer**: Your code (Python, Java, etc.) interacting with Llama Stack APIs.
2.  **API Layer (The Interface)**: Standardized endpoints for Inference, Agents, Safety, Memory, and Evaluation.
3.  **Provider Layer (The Implementation)**: Pluggable backends that do the actual work.
    *   *Inference Provider*: Ollama, TGI, vLLM, Fireworks AI, etc.
    *   *Memory Provider*: FAISS, pgvector, ChromaDB.
    *   *Safety Provider*: Llama Guard, Prompt Guard.

### Why use it?
*   **No Vendor Lock-in**: Switch from local Ollama to cloud-hosted Llama 3.3 without changing a single line of application code.
*   **Standardization**: Unified way to handle tool calling and memory across different models.

---

## 3. Agent Orchestration & Primitives

Llama Stack provides a high-level **Agents API** that abstracts the complexity of managing agent loops.

### How it Orchestrates Agents
Instead of you writing the `while` loop that parses model output, calls tools, and feeds results back, Llama Stack handles this:
1.  **Turn Management**: You send a user message to the `/agent/turn` endpoint.
2.  **Execution Loop**: The stack automatically:
    *   Queries the model.
    *   Detects tool calls.
    *   Executes tools (if configured as "system" tools) or requests execution.
    *   Updates memory/context.
    *   Returns the final response.

### Agent Primitives provided to Agents
*   **Memory**: Built-in short-term (conversation history) and long-term (vector store) memory.
*   **Tools**: Standardized interface for defining tools (Python functions, API calls).
*   **Safety**: Automatic input/output filtering via Llama Guard.
*   **Sessions**: Persistent conversation state management.

### Storage & Tool Calling
*   **Storage**: Managed via the **Memory API**. Agents can query "Banks" (vector stores) or "Key-Value" stores. The stack handles the embedding and retrieval logic.
*   **Tool Calling**:
    *   **Definition**: Tools are defined using the **Model Context Protocol (MCP)** or simple JSON schemas.
    *   **Execution**:
        *   *Client-side*: The stack returns a `tool_call` event, your app executes it, and sends back the result.
        *   *Server-side*: The stack executes the tool directly (e.g., a web search tool or code interpreter running in a sandbox).

---

## 4. OpenShift & OpenShift AI Integration

Llama Stack is a "first-class citizen" on OpenShift.

### Integration Points
*   **Llama Stack Operator**: A Kubernetes Operator specifically for deploying Llama Stack distributions on OpenShift. It manages scaling, configuration, and updates.
*   **OpenShift AI (RHOAI)**: Llama Stack serves as the **unified runtime** for RHOAI. It allows you to serve models deployed in RHOAI (using vLLM or TGI) through the standardized Llama Stack API.
*   **Security**: Leverages OpenShift's RBAC and security context constraints (SCC) for secure agent deployment.

### Deployment Pattern
1.  Install **Llama Stack Operator** from OperatorHub.
2.  Define a `LlamaStackDistribution` CRD (Custom Resource Definition) specifying your desired providers (e.g., vLLM for inference, persistent volume for memory).
3.  The operator spins up the API server and sidecars.

---

## 5. Java Agent Support

Currently, Llama Stack **does not have an official Java Client SDK** (unlike Python, Node.js, and Swift).

### How to Manage Java Agents
Since Llama Stack exposes standard **REST** and **gRPC** endpoints, Java agents can fully utilize the stack.

**Integration Strategy for Java:**
1.  **REST API**: Use `OkHttp` or `Spring RestTemplate` to call the Llama Stack endpoints directly.
    *   *Endpoint*: `POST /v1/agents/{agent_id}/turn`
2.  **OpenAPI Generator**: Generate a robust Java client library from the official `openapi.json` spec provided by the Llama Stack server.

### Tool Calling for Java Agents
Since the Java code holds the tool logic, you will use the **Client-side Tool Execution** pattern:

1.  **Define Tool**: Register the tool definition (JSON schema) with the Llama Stack Agent.
2.  **Agent Turn**: Java app sends user query to Agent API.
3.  **Tool Call Request**: Stack responds with a `tool_execution_request` event (e.g., `call function 'get_weather' with args '{"city": "London"}'`).
4.  **Execution**: Java app detects this event, executes its internal `getWeather(String city)` Java method.
5.  **Report Result**: Java app sends the result back to the Agent API via the `/agent/turn/update` or similar endpoint.
6.  **Final Response**: Stack generates the natural language answer using the tool result.

### Summary Table: Java vs. Python
| Feature | Python Agent | Java Agent |
| :--- | :--- | :--- |
| **SDK** | Official `llama-stack-client` | Generate via OpenAPI / REST |
| **Tool Execution** | Can be Server-side (if Python) or Client-side | **Client-side only** (mostly) |
| **Orchestration** | Managed by Stack or Client | Managed by Stack (via API) |
