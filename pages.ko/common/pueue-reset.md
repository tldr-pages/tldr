# pueue reset

> 모든 작업을 종료하고 재설정.
> 더 많은 정보: <https://github.com/Nukesor/pueue>.

- 모든 작업을 종료하고 모든 것을 제거(로그, 상태, 그룹, 작업 ID):

`pueue reset`

- 모든 작업을 종료하고 그들의 자식 프로세스를 종료한 후 모든 것을 재설정:

`pueue reset --children`

- 확인을 요구하지 않고 재설정:

`pueue reset --force`
