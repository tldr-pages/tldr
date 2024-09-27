# gcrane completion

> Generate the autocompletion script for gcrane for the specified shell.
> The available shells are `bash`, `fish`, `powershell`, and `zsh`.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Display help:

`gcrane completion {{-h|--help}}`

- Generate the autocompletion script for your shell:

`gcrane completion {{shell}}`

- Display help:

`gcrane completion {{shell}} {{-h|--help}}`

- Disable completion descriptions:

`grance completion {{shell}} {{no-descriptions}}`

- Load completions in your current shell session (other OSes available at link):

`source <(gcrane completion bash)>`

- Load completions for every new sesion:

`gcrane completion bash > /etc/bash_completion.d/gcrane (linux)`
