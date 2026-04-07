# autoload

> Zsh에서 함수의 지연 로딩을 설정.
> 함수는 처음 호출될 때 메모리에 로드되어, 쉘 시작 속도를 향상.
> 더 많은 정보: <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>.

- 함수 이름으로 Autoload 설정:

`autoload {{함수_이름}}`

- 함수 Autoload 후 즉시 정의 로드:

`autoload +X {{함수_이름}}`

- Zsh 방식으로 autoload 설정 (권장):

`autoload -Uz {{함수_이름}}`

- 디렉터리를 `fpath`에 추가하여 함수 사용 가능하게 설정:

`fpath=({{경로/대상/함수_폴더}} $fpath) && autoload -Uz {{함수_이름}}`

- Zsh 자동 완성 시스템 Autoload:

`autoload -Uz compinit && compinit`

- `add-zsh-hook` 유틸리티 autoload:

`autoload -Uz add-zsh-hook`
