# gcrane completion

> Generate the autocompletion script for gcrane for the specified shell.
> The available shells are `bash`, `fish`, `powershell`, and `zsh`.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Generate the autocompletion script for your shell:

`gcrane completion {{shell_name}}`

- Disable completion descriptions:

`gcrane completion {{shell_name}} --no-descriptions`

- Load completions in your current shell session (powershell):

`gcrane completion powershell | Out-String | Invoke-Expression`

- Load completions for every new session (powershell):

`gcrane completion powershell | Out-String | Invoke-Expression`

- Display help:

`gcrane completion {{shell_name}} {{[-h|--help]}}`
