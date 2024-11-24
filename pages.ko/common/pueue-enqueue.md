# pueue enqueue

> 저장된 작업을 대기열에 추가.
> 같이 보기: `pueue stash`.
> 더 많은 정보: <https://github.com/Nukesor/pueue>.

- 여러 저장된 작업을 한 번에 대기열에 추가:

`pueue enqueue {{작업_아이디}} {{작업_아이디}}`

- 60초 후에 저장된 작업을 대기열에 추가:

`pueue enqueue --delay {{60}} {{작업_아이디}}`

- 다음 수요일에 저장된 작업을 대기열에 추가:

`pueue enqueue --delay {{wednesday}} {{작업_아이디}}`

- 4개월 후에 저장된 작업을 대기열에 추가:

`pueue enqueue --delay "4 months" {{작업_아이디}}`

- 2021-02-19에 저장된 작업을 대기열에 추가:

`pueue enqueue --delay {{2021-02-19}} {{작업_아이디}}`

- 사용 가능한 모든 날짜/시간 형식 나열:

`pueue enqueue --help`
