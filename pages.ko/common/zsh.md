# zsh

> Z SHell, Bash 호환 명령줄 인터프리터.
> 같이 보기: `bash`, `histexpand`.
> 더 많은 정보: <https://zsh.sourceforge.io/Doc/Release/Invocation.html#Invocation>.

- 대화형 셸 세션 시작:

`zsh`

- 특정 [c]명령 실행:

`zsh -c "{{echo Hello world}}"`

- 특정 스크립트 실행:

`zsh {{경로/대상/스크립트.zsh}}`

- 특정 스크립트를 실행하지 않고 구문 오류 검사:

`zsh --no-exec {{경로/대상/스크립트.zsh}}`

- `stdin`에서 특정 명령 실행:

`{{echo Hello world}} | zsh`

- 특정 스크립트를 실행하며 각 명령을 실행 전에 출력:

`zsh --xtrace {{경로/대상/스크립트.zsh}}`

- 대화형 셸 세션을 자세한 모드로 시작하여 실행 전 각 명령 출력:

`zsh --verbose`

- `zsh` 내에서 특정 명령을 글로브 패턴 비활성화하여 실행:

`noglob {{명령}}`
