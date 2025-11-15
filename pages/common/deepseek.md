# deepseek

> A command-line interface for interacting with DeepSeek language models.
> More information: <https://github.com/deepseek-ai>.

- Run a prompt using the default DeepSeek model:

`deepseek "{{write a haiku about the ocean}}"`

- Specify a model to use:

`deepseek --model {{deepseek-chat}} "{{explain quantum tunneling}}"`

- Run the model with a system instruction:

`deepseek --system "{{You are a helpful assistant.}}" "{{summarize this text}}"`

- Stream the response token-by-token:

`deepseek --stream "{{what is the capital of Japan?}}"`

- Provide input from a file:

`deepseek --input {{path/to/file.txt}}`

- Show help for available flags:

`deepseek --help`
