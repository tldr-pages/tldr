# sleep

> 지정된 시간만큼 지연합니다.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/sleep-invocation.html>.

- 초 단위로 지연:

`sleep {{초}}`

- [m]분 단위로 지연 (다른 단위로는 [d]일, [h]시간, [s]초, [inf]무한대 사용 가능):

`sleep {{분}}m`

- 1[d]일 3[h]시간 동안 지연:

`sleep 1d 3h`

- 20[m]분 지연 후 특정 명령 실행:

`sleep 20m && {{명령}}`
