# base64

> 파일 또는 `stdin`을 base64로 인코딩하거나 디코딩하여 `stdout` 또는 다른 파일로 출력.
> 더 많은 정보: <https://man.freebsd.org/cgi/man.cgi?query=base64>.

- 파일을 인코딩하여 `stdout`으로 출력:

`base64 {{[-i|--input]}} {{경로/대상/파일}}`

- 파일을 인코딩하여 지정된 출력 파일로 저장:

`base64 {{[-i|--input]}} {{경로/대상/입력_파일}} {{[-o|--output]}} {{경로/대상/출력_파일}}`

- 특정 너비로 인코딩된 출력 줄바꿈 (`0`은 줄바꿈 비활성화):

`base64 {{[-b|--break]}} {{0|76|...}} {{경로/대상/파일}}`

- 파일을 디코딩하여 `stdout`으로 출력:

`base64 {{[-d|--decode]}} {{[-i|--input]}} {{경로/대상/파일}}`

- `stdin`을 인코딩하여 `stdout`으로 출력:

`{{명령어}} | base64`

- `stdin`을 디코딩하여 `stdout`으로 출력:

`{{명령어}} | base64 {{[-d|--decode]}}`
