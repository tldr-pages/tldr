# dotty

> X Window System용 커스텀 가능한 대화형 그래프 편집기.
> 참고: 이 도구는 더이상 유지 안 되지만, 기존 사용자들을 위해 항목이 유지됨.
> 더 많은 정보: <https://graphviz.org/pdf/dotty.1.pdf>.

- 그래프 파일(`.gv` 또는 `.dot`)을 Dotty 편집기로 열기:

`dotty {{경로/대상/그래프.gv}}`

- 버전([V]ersion) 정보를 표시하며 Dotty 실행:

`dotty -V`

- 레이아웃 모드([l]ayout [m]ode)를 동기 또는 비동기로 설정:

`dotty -lm {{sync|async}} {{경로/대상/그래프.gv}}`

- 메시지(m[e]ssage) 출력 레벨([l]evel) (`0`: 최소, `1`: 상세):

`dotty -el {{0|1}} {{경로/대상/그래프.gv}}`
