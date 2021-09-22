# starship

> The minimal, blazing-fast, and infinitely customizable prompt for any shell.
> Some subcommands such as `starship init` have their own usage documentation.
> More information: <https://starship.rs>.

- Print the starship integration code for the specified shell:

`starship init {{bash|elvish|fish|ion|powershell|tcsh|zsh}}`

- Explain each part of the current prompt and show the time taken to render them:

`starship explain`

- Print the computed starship configuration (use `--default` to print default configuration instead):

`starship print-config`

- List supported modules:

`starship module --list`

- Edit the starship configuration in the default editor:

`starship configure`

- Create a bug report GitHub issue pre-populated with information about the system and starship configuration:

`starship bug-report`

- Print the completion script for the specified shell:

`starship completions {{bash|elvish|fish|powershell|zsh}}`

- Display help for a subcommand:

`starship {{subcommand}} --help`
