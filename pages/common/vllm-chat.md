# vllm chat

> Generate chat completions via the running API server using the OpenAI-compatible REST API.
> More information: <https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html>.

- Send a single chat prompt to the API server and get a response:

`vllm chat --quick "{{message}}"`

- Chat with a specific model name:

`vllm chat --model-name {{model_name}} --quick "{{message}}"`

- Chat with a custom system prompt:

`vllm chat --system-prompt "{{system_prompt}}" --quick "{{message}}"`

- Chat using a custom API server URL:

`vllm chat --url {{http://custom-host:port/v1}} --quick "{{message}}"`

- Chat with an API key for authentication:

`vllm chat --api-key {{your_api_key}} --quick "{{message}}"`

- Start an interactive chat session:

`vllm chat`
