# nice

> 사용자 지정 스케줄링 우선순위(niceness)로 프로그램을 실행.
> Niceness 값의 범위는 -20(가장 높은 우선순위)부터 19(가장 낮은 우선순위)를 가짐.
> > 참고: 일부 최신 스케줄러는 niceness를 무시하거나 autogroup 내에서 그 효과를 제한할 수 있음.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/nice-invocation.html>.

- 현재 niceness 값 출력:

`nice`

- 현재 niceness 값을 10만큼 증가:

`nice nice`

- 낮은 우선순위로 프로그램 실행:

`nice -{{niceness_값}} {{명령어}}`

- 높은 우선순위로 프로그램 실행:

`sudo nice --{{niceness_값}} {{명령어}}`

- 명시적인 옵션으로 우선순위 지정:

`nice {{[-n|--adjustment]}} {{niceness_값}} {{명령어}}`
