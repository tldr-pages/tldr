# starship init

> Print shell integration code for starship.
> More information: <https://starship.rs>.

- Display the subcommand help:

`starship init --help`

- Print the starship integration code for the specified shell:

`starship init {{bash|elvish|fish|ion|powershell|tcsh|zsh}}`

- Append the `starship` integration code to `~/.bashrc`:

`starship init {{bash}} >> {{~/.bashrc}}`

- Append the `starship` integration code to `~/.zshrc`:

`starship init {{zsh}} >> {{~/.zshrc}}`
