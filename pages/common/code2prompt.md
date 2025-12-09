# code2prompt

> Generate AI-ready prompts from a codebase (extracts, filters and formats code for LLMs).
> More information: <https://code2prompt.dev/docs/how_to/filter_files/>.

- Generate a prompt for the current project and copy it to the clipboard (default behaviour):

`code2prompt {{path/to/project}}`

- Include only specific files and exclude a directory:

`code2prompt {{path/to/project}} {{[-i|--include]}} "{{**/*.rs}}" {{[-e|--exclude]}} "{{tests/**}}"`

- Write the prompt to a file instead of the clipboard:

`code2prompt {{path/to/project}} {{[-O|--output-file]}} {{my_prompt.txt}}`

- Produce structured JSON output:

`code2prompt {{path/to/project}} {{[-F|--output-format]}} json`

- Use a custom Handlebars template when generating the prompt:

`code2prompt {{path/to/project}} {{[-t|--template]}} {{my_template.hbs}}`
