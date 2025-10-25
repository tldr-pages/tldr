# tv

> Cross-platform, fast, extensible fuzzy-finder tool.
> Works with “channels” (e.g., files, env, git repos) or from `stdin`.
> More information: <https://alexpasmantier.github.io/television/>.

- Launch with the default channel:

`tv`

- Open a specific channel:

`tv {{files|env|git-repos|...}}`

- List all available channels:

`tv list-channels`

- Fuzzy-pick from lines piped on standard input:

`{{command}} | tv`

- Pipe and show a live preview for each entry:

`{{command}} | tv --preview '{{preview_command}}'`

- Build a picker from commands (source + preview):

`tv --source-command '{{source_command}}' --preview-command '{{preview_command}}' --preview-size {{70}}`

- Update and install community-maintained channels:

`tv update-channels`
