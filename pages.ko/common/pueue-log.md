# pueue log

> 하나 이상의 작업에 대한 로그 출력을 표시합니다.
> 같이 보기: `pueue status`.
> 더 많은 정보: <https://github.com/Nukesor/pueue>.

- 모든 작업의 마지막 몇 줄의 출력 표시:

`pueue log`

- 특정 작업의 전체 출력 표시:

`pueue log {{작업_아이디}}`

- 여러 작업의 마지막 몇 줄의 출력 표시:

`pueue log {{작업_아이디}} {{작업_아이디}}`

- 출력의 끝에서 특정 줄 수 만큼의 줄을 출력:

`pueue log --lines {{number_of_lines}} {{작업_아이디}}`
