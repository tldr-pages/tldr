# aider

> Pair program with the LLM of your choice.
> More information: <https://github.com/Aider-AI/aider>.

- Start a new project or work with an existing code base:

`aider --model {{model_name}} --api-key {{your_api_key}}`

- Add new features or test cases to specific files:

`aider {{path/to/file1 path/to/file2 ...}}`

- Describe a bug and let `aider` fix it:

`aider {{path/to/file}} --describe "{{bug_description}}"`

- Refactor code in a specific file:

`aider {{path/to/file}} --refactor`

- Update documentation:

`aider {{path/to/file}} --update-docs`

- Display help:

`aider --help`
