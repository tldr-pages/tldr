# tload

> 시스템 load average를 ASCII 그래프로 표시하는 도구.
> 관련 항목: `uptime`, `w`, `top`, `ps`.
> 더 많은 정보: <https://manned.org/tload>.

- Run tload 실행:

`tload`

- 특정 세로 스케일로 그래프 표시 (e.g. 10 -> 1:1 스케일):

`tload {{[-s|--scale]}} {{값}}`

- 그래프 갱신 주기 설정:

`tload {{[-d|--delay]}} {{초}}`

- 특정 터미널에 그래프 표시:

`tload {{/dev/tty1}}`
