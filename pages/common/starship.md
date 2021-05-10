# starship

> The minimal, blazing-fast, and infinitely customizable prompt for any shell.
> More information: <https://starship.rs>.

- Print the starship integration code for the specified shell:

`starship init {{bash|elvish|fish|ion|powershell|tcsh|zsh}}`

- Explain the current showing modules:

`starship explain`

- Print the computed starship configuration (use `--default` to print default configuration instead):

`starship print-config`

- List supported modules:

`starship module --list`

- Edit the starship configuration in the default editor:

`starship configure`

- Create a pre-populated GitHub issue with information about your configuration:

`starship bug-report`

- Print a completion script:

`starship completions {{bash|elvish|fish|powershell|zsh}}`

- Display help for a subcommand:

`starship {{subcommand}} --help`
