# kubectl completion

> Generate shell completion code for `kubectl` commands.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_completion/>.

- Print the completion script for Bash, Zsh, fish, or PowerShell:

`kubectl completion {{bash|zsh|fish|powershell}}`

- Load Bash or Zsh completions into the current shell session:

`source <(kubectl completion {{bash|zsh}})`

- Append Bash completion script to `~/.bashrc`:

`kubectl completion bash >> ~/.bashrc`

- Write Zsh completion script to a file in the `fpath`:

`kubectl completion zsh > "${fpath[1]}/_kubectl"`

- Load fish completions into the current shell session:

`kubectl completion fish | source`

- Persist fish completions:

`kubectl completion fish > ~/.config/fish/completions/kubectl.fish`

- Load PowerShell completions into the current shell session:

`kubectl completion powershell | Out-String | Invoke-Expression`

- Persist PowerShell completions:

`kubectl completion powershell >> $PROFILE`
