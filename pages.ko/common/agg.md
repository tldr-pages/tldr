# agg

> `asciinema` 터미널 세션 녹화로부터 GIF를 생성.
> 더 많은 정보: <https://docs.asciinema.org/manual/agg/usage/>.

- GIF 생성:

`agg {{경로/대상/demo.cast}} {{경로/대상/demo.gif}}`

- 너비 80열, 높이 25행 크기의 GIF를 생성:

`agg --cols 80 --rows 25 {{경로/대상/demo.cast}} {{경로/대상/demo.gif}}`

- 글꼴 크기 24픽셀로 GIF를 생성:

`agg --font-size 24 {{경로/대상/demo.cast}} {{경로/대상/demo.gif}}`

- 도움말 표시:

`agg {{[-h|--help]}}`
