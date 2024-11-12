# pueue pause

> 실행 중인 작업 또는 그룹 일시 중지.
> 같이 보기: `pueue start`.
> 더 많은 정보: <https://github.com/Nukesor/pueue>.

- 기본 그룹의 모든 작업 일시 중지:

`pueue pause`

- 실행 중인 작업 일시 중지:

`pueue pause {{작업_아이디}}`

- 실행 중인 작업과 그 직접적인 하위 작업 모두 일시 중지:

`pueue pause --children {{작업_아이디}}`

- 그룹 내 모든 작업을 일시 중지하고 새로운 작업 시작 방지:

`pueue pause --group {{그룹_이름}}`

- 모든 작업을 일시 중지하고 모든 그룹의 새로운 작업 시작 방지:

`pueue pause --all`
