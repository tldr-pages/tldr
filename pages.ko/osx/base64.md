# base64

> 파일 또는 `stdin`을 base64로 인코딩하거나 디코딩하여 `stdout` 또는 다른 파일로 출력.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/bintrans.1>.

- 파일을 `stdout`으로 인코딩:

`base64 {{[-i|--input]}} {{경로/대상/파일}}`

- 파일을 지정된 출력 파일로 인코딩:

`base64 {{[-i|--input]}} {{경로/대상/입력_파일}} {{[-o|--output]}} {{경로/대상/출력_파일}}`

- 인코딩된 출력을 특정 너비로 줄 바꿈 (`0`은 줄 바꿈 비활성화):

`base64 {{[-b|--break]}} {{0|76|...}} {{경로/대상/파일}}`

- 파일을 `stdout`으로 디코딩:

`base64 {{[-d|--decode]}} {{[-i|--input]}} {{경로/대상/파일}}`

- `stdin`에서 `stdout`으로 인코딩:

`{{command}} | base64`

- `stdin`에서 `stdout`으로 디코딩:

`{{command}} | base64 {{[-d|--decode]}}`
