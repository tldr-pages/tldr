# gcrane completion

> 지정된 셸에 대한 gcrane 자동 완성 스크립트를 생성합니다.
> 사용할 수 있는 셸은 `bash`, `fish`, `powershell`, `zsh`입니다.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- 셸에 대한 자동 완성 스크립트 생성:

`gcrane completion {{셸_이름}}`

- 자동 완성 설명 비활성화:

`gcrane completion {{셸_이름}} --no-descriptions`

- 현재 셸 세션에서 자동 완성 로드 (bash/zsh):

`source <(gcrane completion bash/zsh)`

- 현재 셸 세션에서 자동 완성 로드 (fish):

`gcrane completion fish | source`

- 매 새로운 세션에서 자동 완성 로드 (bash):

`gcrane completion bash > $(brew --prefix)/etc/bash_completion.d/gcrane`

- 매 새로운 세션에서 자동 완성 로드 (zsh):

`gcrane completion zsh > $(brew --prefix)/share/zsh/site-functions/_gcrane`

- 매 새로운 세션에서 자동 완성 로드 (fish):

`gcrane completion fish > ~/.config/fish/completions/gcrane.fish`

- 도움말 표시:

`gcrane completion {{셸_이름}} {{[-h|--help]}}`
