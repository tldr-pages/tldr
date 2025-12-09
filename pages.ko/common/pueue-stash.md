# pueue stash

> 작업을 자동으로 시작하지 않도록 임시 저장.
> 같이 보기: `pueue start` 및 `pueue enqueue`.
> 더 많은 정보: <https://github.com/Nukesor/pueue>.

- 대기열에 있는 작업 임시 저장:

`pueue stash {{작업_아이디}}`

- 여러 작업을 한 번에 임시 저장:

`pueue stash {{작업_아이디}} {{작업_아이디}}`

- 임시 저장된 작업을 즉시 시작:

`pueue start {{작업_아이디}}`

- 선행 작업이 완료되면 실행하도록 작업 대기열에 추가:

`pueue enqueue {{작업_아이디}}`
