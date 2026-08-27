# llm prompt

> Execute a prompt using a Large Language Model.
> More information: <https://llm.datasette.io/en/stable/usage.html#executing-a-prompt>.

- Execute a prompt using the default model:

`llm prompt "{{Ten fun names for a pet pelican}}"`

- Execute a prompt with a specific model and system prompt:

`llm prompt "{{Explain quantum entanglement}}" {{[-m|--model]}} {{model_name}} {{[-s|--system]}} "{{Answer concisely}}"`

- Execute a prompt with an attachment:

`llm prompt "{{Describe this image}}" {{[-a|--attachment]}} {{path/to/image.jpg}}`

- Request structured JSON using a concise schema:

`llm prompt "{{Invent a dog}}" --schema "{{name, age int, active bool}}"`

- Continue the most recent conversation:

`llm prompt "{{What about Germany?}}" {{[-c|--continue]}}`

- Extract the first fenced code block from the response:

`llm prompt "{{Write a JavaScript function that reverses a string}}" {{[-x|--extract]}}`
