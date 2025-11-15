# code2prompt

> Generate AI-ready prompts from a codebase (extracts, filters and formats code for LLMs).
> More information: <https://code2prompt.dev/docs/tutorials/getting_started/>.

- Generate a prompt for the current project and copy it to the clipboard (default behaviour):

`code2prompt {{path/to/project}}`

- Include only specific files and exclude a directory:

`code2prompt {{path/to/project}} --include "{{**/*.rs}}" --exclude "{{tests/**}}"`

- Write the prompt to a file instead of the clipboard:

`code2prompt {{path/to/project}} --output-file {{my_prompt.txt}}`

- Produce structured JSON output:

`code2prompt {{path/to/project}} --output-format {{json}}`

- Use a custom Handlebars template when generating the prompt:

`code2prompt {{path/to/project}} --template {{my_template.hbs}}`

- Run as an MCP server for dynamic agent integration (advanced):

`code2prompt server --port {{1234}}`
