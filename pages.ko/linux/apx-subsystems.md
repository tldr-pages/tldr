# apx subsystems

> `apx`에서 서브시스템을 관리합니다.
> 서브시스템은 기존 스택을 기반으로 생성될 수 있는 컨테이너입니다.
> 더 많은 정보: <https://docs.vanillaos.org/docs/en/apx-manpage#subsystems>.

- 새 서브시스템을 대화식으로 생성:

`apx subsystems new`

- 사용 가능한 모든 서브시스템 나열:

`apx subsystems list`

- 특정 서브시스템을 초기 상태로 재설정:

`apx subsystems reset {{[-n|--name]}} {{문자열}}`

- 특정 서브시스템을 [f]강제로 재설정:

`apx subsystems reset {{[-n|--name]}} {{문자열}} {{[-f|--force]}}`

- 특정 서브시스템 제거:

`apx subsystems rm {{[-n|--name]}} {{문자열}}`

- 특정 서브시스템을 [f]강제로 제거:

`apx subsystems rm {{[-n|--name]}} {{문자열}} {{[-f|--force]}}`
