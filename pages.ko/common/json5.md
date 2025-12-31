# json5

> JSON5 파일을 JSON으로 변환.
> 더 많은 정보: <https://json5.org/#cli>.

- JSON5 `stdin`을 JSON `stdout`으로 변환:

`echo {{입력}} | json5`

- JSON5 파일을 JSON으로 변환하여 `stdout`으로 출력:

`json5 {{경로/대상/입력_파일.json5}}`

- JSON5 파일을 지정된 JSON 파일로 변환:

`json5 {{경로/대상/입력_파일.json5}} --out-file {{경로/대상/출력_파일.json}}`

- JSON5 파일 유효성 검사:

`json5 {{경로/대상/입력_파일.json5}} --validate`

- 들여쓰기할 공백 수를 지정 (또는 "t"로 탭 사용):

`json5 --space {{들여쓰기_수량}}`

- 도움말 표시:

`json5 --help`
