# kubectl completion

> Генерировать код автодополнения для команд `kubectl`.
> Больше информации: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_completion/>.

- Вывести скрипт автодополнения для Bash, Zsh, fish или PowerShell:

`kubectl completion {{bash|zsh|fish|powershell}}`

- Загрузить автодополнение Bash или Zsh в текущую сессию оболочки:

`source <(kubectl completion {{bash|zsh}})`

- Добавить скрипт автодополнения Bash в `~/.bashrc`:

`kubectl completion bash >> ~/.bashrc`

- Записать скрипт автодополнения Zsh в файл в `fpath`:

`kubectl completion zsh > "${fpath[1]}/_kubectl"`

- Загрузить автодополнение fish в текущую сессию оболочки:

`kubectl completion fish | source`

- Сохранить автодополнение fish:

`kubectl completion fish > ~/.config/fish/completions/kubectl.fish`

- Загрузить автодополнение PowerShell в текущую сессию оболочки:

`kubectl completion powershell | Out-String | Invoke-Expression`

- Сохранить автодополнение PowerShell:

`kubectl completion powershell >> $PROFILE`
