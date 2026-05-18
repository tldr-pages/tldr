# litellm

> Call 100+ LLM APIs using the OpenAI format. Supports OpenAI, Anthropic, Cohere, and more.
> More information: <https://docs.litellm.ai/docs/proxy/cli>.

- Start the LiteLLM proxy server:

  `litellm --model {{openai/gpt-4o}}`

- Start the proxy on a specific port:

  `litellm --model {{anthropic/claude-sonnet-4-5}} --port {{4000}}`

- Start the proxy with a config file:

  `litellm --config {{path/to/config.yaml}}`

- Test the proxy with a sample request:

  `litellm --test`

- Display version:

  `litellm --version`
