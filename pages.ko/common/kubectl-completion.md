# kubectl completion

> `kubectl` 명령어용 쉘 자동 완성 코드 생성.
> 더 많은 정보: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_completion/>.

- Bash, Zsh, fish, 또는 PowerShell용 자동 완성 스크립트 출력:

`kubectl completion {{bash|zsh|fish|powershell}}`

- Bash 또는 Zsh 자동 완성을 현재 쉘 세션에 로드:

`source <(kubectl completion {{bash|zsh}})`

- Bash 자동 완성 스크립트를 `~/.bashrc`에 추가:

`kubectl completion bash >> ~/.bashrc`

- Zsh 자동 완성 스크립트를 `fpath` 디렉터리에 저장:

`kubectl completion zsh > "${fpath[1]}/_kubectl"`

- fish 자동 완성을 현재 쉘 세션에 로드:

`kubectl completion fish | source`

- fish 자동완성을 영구적으로 저장:

`kubectl completion fish > ~/.config/fish/completions/kubectl.fish`

- PowerShell 자동 완성을 현재 세션에 로드:

`kubectl completion powershell | Out-String | Invoke-Expression`

- PowerShell 자동완성을 영구 저장:

`kubectl completion powershell >> $PROFILE`
