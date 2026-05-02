# aichat

> All-in-one LLM CLI tool with Shell Assistant, Chat-REPL, RAG, and AI Agents.
> Supports 20+ providers including OpenAI, Claude, Gemini, and Ollama.
> More information: <https://github.com/sigoden/aichat>.

- Start an interactive chat session:

`aichat`

- Send a single prompt and print the response:

`aichat "{{What is the capital of France?}}"`

- Use a specific model:

`aichat --model {{claude:claude-opus-4-7}} "{{prompt}}"`

- Generate and execute a shell command from a natural language description:

`aichat --execute "{{list all running docker containers}}"`

- Pipe content as context:

`cat {{path/to/file.txt}} | aichat "{{summarize this}}"`
