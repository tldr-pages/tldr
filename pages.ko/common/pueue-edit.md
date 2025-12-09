# pueue edit

> 저장되거나 대기 중인 작업의 명령어나 경로를 편집.
> 더 많은 정보: <https://github.com/Nukesor/pueue>.

- 작업 편집, 작업 ID를 확인하려면 `pueue status` 사용:

`pueue edit {{작업_아이디}}`

- 작업이 실행되는 경로 편집:

`pueue edit {{작업_아이디}} --path`

- 지정된 편집기로 명령어 편집:

`EDITOR={{nano}} pueue edit {{작업_아이디}}`
