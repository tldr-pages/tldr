# gh completion

> Generate shell completion scripts for GitHub CLI commands.
> More information: <https://cli.github.com/manual/gh_completion>.

- Print a completion script:

`gh completion {{[-s|--shell]}} {{bash|zsh|fish|powershell}}`

- Append the `gh` completion script to `~/.bashrc`:

`gh completion {{[-s|--shell]}} bash >> ~/.bashrc`

- Append the `gh` completion script to `~/.zshrc`:

`gh completion {{[-s|--shell]}} zsh >> ~/.zshrc`

- Display the subcommand help:

`gh completion`
