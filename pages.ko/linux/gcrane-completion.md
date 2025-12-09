# gcrane completion

> 지정된 셸에 대한 gcrane 자동 완성 스크립트를 생성합니다.
> 사용 가능한 셸은 `bash`, `fish`, `powershell`, `zsh`입니다.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- 셸에 대한 자동 완성 스크립트 생성:

`gcrane completion {{셸_이름}}`

- 완성 설명 비활성화:

`gcrane completion {{셸_이름}} --no-descriptions`

- 현재 셸 세션에서 완성 로드 (bash/zsh):

`source <(gcrane completion bash/zsh)`

- 현재 셸 세션에서 완성 로드 (fish):

`gcrane completion fish | source`

- 새로운 세션마다 완성 로드 (bash):

`gcrane completion bash > /etc/bash_completion.d/gcrane`

- 새로운 세션마다 완성 로드 (zsh):

`gcrane completion zsh > "${fpath[1]}/_gcrane"`

- 새로운 세션마다 완성 로드 (fish):

`gcrane completion fish > ~/.config/fish/completions/gcrane.fish`

- 도움말 표시:

`gcrane completion {{셸_이름}} {{[-h|--help]}}`
