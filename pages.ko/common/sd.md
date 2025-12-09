# sd

> 직관적인 찾기 및 바꾸기 도구.
> 더 많은 정보: <https://github.com/chmln/sd>.

- 정규식을 사용하여 공백 제거 (출력 스트림: `stdout`):

`{{echo 'lorem ipsum 23   '}} | sd '\s+$' ''`

- 캡처 그룹을 사용하여 단어 바꾸기 (출력 스트림: `stdout`):

`{{echo 'cargo +nightly watch'}} | sd '(\w+)\s+\+(\w+)\s+(\w+)' 'cmd: $1, channel: $2, subcmd: $3'`

- 특정 파일에서 찾기 및 바꾸기 (출력 스트림: `stdout`):

`sd -p {{'window.fetch'}} {{'fetch'}} {{경로/대상/파일.js}}`

- 현재 프로젝트의 모든 파일에서 찾기 및 바꾸기 (출력 스트림: `stdout`):

`sd {{'from "react"'}} {{'from "preact"'}} "$(find . -type f)"`
