# pueue start

> 작업 또는 작업 그룹의 실행을 재개.
> 같이 보기: `pueue pause`.
> 더 많은 정보: <https://github.com/Nukesor/pueue>.

- 기본 그룹의 모든 작업 재개:

`pueue start`

- 특정 작업 재개:

`pueue start {{작업_아이디}}`

- 여러 작업을 동시에 재개:

`pueue start {{작업_아이디}} {{작업_아이디}}`

- 모든 작업과 그 하위 작업 재개:

`pueue start --all --children`

- 특정 그룹의 모든 작업 재개:

`pueue start group {{그룹_이름}}`
