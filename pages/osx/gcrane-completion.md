# gcrane completion

> Generate the autocompletion script for gcrane for the specified shell.
> The available shells are Bash, fish, PowerShell, and Zsh.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Generate the autocompletion script for your shell:

`gcrane completion {{shell_name}}`

- Disable completion descriptions:

`gcrane completion {{shell_name}} --no-descriptions`

- Load completions in your current shell session (Bash/Zsh):

`source <(gcrane completion bash/zsh)`

- Load completions in your current shell session (fish):

`gcrane completion fish | source`

- Load completions for every new session (Bash):

`gcrane completion bash > $(brew --prefix)/etc/bash_completion.d/gcrane`

- Load completions for every new session (Zsh):

`gcrane completion zsh > $(brew --prefix)/share/zsh/site-functions/_gcrane`

- Load completions for every new session (fish):

`gcrane completion fish > ~/.config/fish/completions/gcrane.fish`

- Display help:

`gcrane completion {{shell_name}} {{[-h|--help]}}`
