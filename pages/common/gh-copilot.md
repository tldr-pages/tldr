# gh copilot

> Interact with GitHub Copilot.
> Note: Deprecated in favor of `copilot`.
> More information: <https://github.com/github/gh-copilot#usage>.

- Suggest a command, given a description:

`gh copilot suggest "{{Install git}}"`

- Suggest a Git command:

`gh copilot suggest {{[-t|--target]}} git "{{Undo the most recent local commits}}"`

- Explain a command:

`gh copilot explain "{{traceroute example.com}}"`

- Generate shell-specific aliases for Bash:

`echo 'eval "$(gh copilot alias -- bash)"' >> ~/.bashrc`

- Generate shell-specific aliases for Zsh:

`echo 'eval "$(gh copilot alias -- zsh)"' >> ~/.zshrc`

- Configure options:

`gh copilot config`
