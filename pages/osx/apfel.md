# apfel

> Query Apple Intelligence's on-device language model from the command line.
> Runs fully offline on Apple Silicon; no API key or model download required.
> More information: <https://apfel.franzai.com>.

- Send a single prompt:

`apfel "{{What is the capital of Austria?}}"`

- Stream the response as it is generated:

`apfel --stream "{{prompt}}"`

- Start an interactive chat session with a custom system prompt:

`apfel --system "{{You are a pirate}}" --chat`

- Attach a file's content to the prompt:

`apfel --file {{path/to/file}} "{{prompt}}"`

- Print only the code from the response, without explanation:

`apfel --code "{{prompt}}"`

- Get the response as JSON:

`apfel --output json "{{Translate to German: hello}}"`

- Start a local OpenAI-compatible API server:

`apfel --serve --port {{3000}}`
