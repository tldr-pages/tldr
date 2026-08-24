# ioping

> 실시간으로 디스크 I/O 지연시간을 모니터링하는 도구.
> 더 많은 정보: <https://github.com/koct9i/ioping>.

- 기본 설정으로 현재 디렉터리의 디스크 I/O 지연 시간 확인:

`ioping .`

- `/tmp`에서 1MB 크기로 10회 요청하여 지연 시간 측정:

`ioping {{[-c|-count]}} 10 {{[-s|-size]}} 1M /tmp`

- `/dev/sdX`에서 디스크 탐색 속도 측정:

`ioping {{[-R|-rapid]}} {{/dev/sdX}}`

- `/dev/sdX`에서 디스크 순차 읽기 속도 측정:

`ioping {{[-RL|-rapid -linear]}} {{/dev/sdX}}`
