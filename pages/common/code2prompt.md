# code2prompt

> Convert codebases into LLM prompts with source tree, prompt templating, and token counting.
> More information: <https://code2prompt.dev>.

- Generate a prompt from the current directory:

`code2prompt`

- Generate a prompt from a specific directory:

`code2prompt {{path/to/directory}}`

- Generate a prompt using a custom template:

`code2prompt --template {{path/to/template.hbs}}`

- Generate a prompt and save to a file:

`code2prompt --output {{path/to/output.txt}}`

- Generate a prompt with specified file extensions:

`code2prompt --filter "{{*.py,*.js}}"`

- Display token count for the prompt:

`code2prompt --tokens`

- Exclude specific directories from the prompt:

`code2prompt --exclude "{{node_modules,dist}}"`
