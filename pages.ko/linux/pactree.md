# pactree

> pacman용 패키지 의존성 트리 뷰어.
> 더 많은 정보: <https://manned.org/pactree.8>.

- 특정 패키지의 의존성 트리를 출력:

`pactree {{패키지}}`

- 특정 패키지에 의존하는 패키지 출력:

`pactree {{[-r|--reverse]}} {{패키지}}`

- 중복을 생략하고 의존성을 한 줄에 하나씩 출력:

`pactree {{[-u|--unique]}} {{패키지}}`

- 특정 패키지의 선택적 의존성을 포함하고 출력을 색상으로 표시:

`pactree {{[-co|--color --optional]}} {{패키지}}`

- 도움말 표시:

`pactree`
