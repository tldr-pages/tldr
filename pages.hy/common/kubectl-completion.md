# kubectl ավարտ

> Ստեղծեք կեղևի ավարտման կոդ `kubectl` հրամանների համար:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_completion/>:.

- Տպեք ավարտման սցենարը Bash-ի, Zsh-ի, fish-ի կամ PowerShell-ի համար.:

`kubectl completion {{bash|zsh|fish|powershell}}`

- Ներբեռնեք Bash կամ Zsh լրացումները ընթացիկ shell նիստում.:

`source <(kubectl completion {{bash|zsh}})`

- Կցեք Bash-ի ավարտման սցենարը `~/.bashrc`-ին:

`kubectl completion bash >> ~/.bashrc`

- Գրեք Zsh-ի ավարտի սցենարը `fpath` ֆայլում.:

`kubectl completion zsh > "${fpath[1]}/_kubectl"`

- Ներբեռնեք ձկան լրացումները ընթացիկ կեղևի նստաշրջանում.:

`kubectl completion fish | source`

- Ձկների շարունակական ավարտ.:

`kubectl completion fish > ~/.config/fish/completions/kubectl.fish`

- Ներբեռնեք PowerShell-ի լրացումները ընթացիկ shell նիստում.:

`kubectl completion powershell | Out-String | Invoke-Expression`

- Persist PowerShell ավարտումները.:

`kubectl completion powershell >> $PROFILE`
