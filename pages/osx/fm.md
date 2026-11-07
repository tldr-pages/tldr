# fm

> Interact with Apple Foundation Models, the language models built into macOS.
> More information: <https://keith.github.io/xcode-man-pages/fm.1.html>.

- Review and accept the license terms (required once per machine before first use):

`sudo fm license`

- Generate a response to a prompt:

`fm respond "{{What is Swift?}}"`

- Start an interactive chat session with custom instructions:

`fm chat {{[-i|--instructions]}} "{{You are a coding assistant}}"`

- Process text from `stdin` using instructions (`stdin` is ignored if a prompt is also given):

`cat {{path/to/file.txt}} | fm respond {{[-i|--instructions]}} "{{Summarize this text in two sentences}}"`

- Generate a JSON schema for an object with a string and an integer property:

`fm schema object --name {{Person}} --string {{name}} --int {{age}} > {{path/to/schema.json}}`

- Generate a JSON response that conforms to a schema:

`fm respond "{{Amit is 42 years old}}" --schema {{path/to/schema.json}}`

- Count the tokens in a prompt:

`fm count-tokens "{{Hello world}}"`

- Start an OpenAI-compatible Chat Completions API server on a specific port:

`fm serve --port {{8080}}`
