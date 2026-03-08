# llm chat

> Hold an interactive chat conversation with a Large Language Model.
> See also: `llm`.
> More information: <https://llm.datasette.io/en/stable/help.html>.

- Start an interactive chat session with the default model:

`llm chat`

- Start a chat session with a specific model:

`llm chat {{[-m|--model]}} {{gpt-4o}}`

- Start a chat session with a system prompt:

`llm chat {{[-s|--system]}} "{{You are a helpful coding assistant}}"`

- Continue the most recent chat session:

`llm chat {{[-c|--continue]}}`

- Start a chat session using a saved template:

`llm chat {{[-t|--template]}} {{template_name}}`

- Start a chat session with a tool available to the model:

`llm chat {{[-T|--tool]}} {{tool_name}}`

- Display help:

`llm chat --help`
