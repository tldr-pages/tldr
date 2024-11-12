# gibo

> gitignore 상용구를 가져옴.
> 더 많은 정보: <https://github.com/simonwhitaker/gibo>.

- 사용 가능한 상용구 목록:

`gibo list`

- `stdout`에 상용구를 작성:

`gibo dump {{상용구}}`

- .gitignore에 상용구를 작성:

`gibo dump {{상용구}} >>{{.gitignore}}`

- 주어진 문자열을 포함하는 상용구 검색:

`gibo search {{문자열}}`

- 사용 가능한 로컬 상용구 업데이트:

`gibo update`
