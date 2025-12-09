# pueue kill

> 실행 중인 작업이나 전체 그룹을 종료.
> 더 많은 정보: <https://github.com/Nukesor/pueue>.

- 기본 그룹의 모든 작업 종료:

`pueue kill`

- 특정 작업 종료:

`pueue kill {{작업_아이디}}`

- 작업과 해당 자식 프로세스 모두 종료:

`pueue kill --children {{작업_아이디}}`

- 그룹의 모든 작업 종료 및 그룹 일시 중지:

`pueue kill --group {{그룹_이름}}`

- 모든 그룹의 모든 작업 종료 및 모든 그룹 일시 중지:

`pueue kill --all`
