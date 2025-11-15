# nice

> 프로그램을 사용자 정의 스케줄링 우선순위(친화도)로 실행.
> 친화도 값은 -20(가장 높은 우선순위)에서 19(가장 낮은 우선순위)까지 범위.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/nice-invocation.html>.

- 변경된 우선순위로 프로그램 실행:

`nice -{{친화도_값}} {{명령어}}`

- 명시적 옵션으로 우선순위 정의:

`nice {{[-n|--adjustment]}} {{친화도_값}} {{명령어}}`
