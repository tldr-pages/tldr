# pueue follow

> 현재 실행 중인 작업의 출력을 따라가기.
> 같이 보기: `pueue log`.
> 더 많은 정보: <https://github.com/Nukesor/pueue>.

- 작업의 출력(`stdout` + `stderr`)을 따라가기:

`pueue follow {{작업_아이디}}`

- 작업의 `stderr`를 따라가기:

`pueue follow --err {{작업_아이디}}`
