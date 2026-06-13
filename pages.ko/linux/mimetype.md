# mimetype

> 파일의 MIME 유형을 자동으로 결정합니다.
> 더 많은 정보: <https://manned.org/mimetype>.

- 주어진 파일의 MIME 유형 출력:

`mimetype {{경로/대상/파일}}`

- 파일명을 제외하고 MIME 유형만 표시:

`mimetype --brief {{경로/대상/파일}}`

- MIME 유형 설명 표시:

`mimetype --describe {{경로/대상/파일}}`

- `stdin`의 MIME 유형 결정 (파일명 확인하지 않음):

`{{command}} | mimetype --stdin`

- MIME 유형이 결정된 방법에 대한 디버그 정보 표시:

`mimetype --debug {{경로/대상/파일}}`

- 주어진 파일의 가능한 모든 MIME 유형을 신뢰도 순으로 표시:

`mimetype --all {{경로/대상/파일}}`

- 출력의 2글자 언어 코드를 명시적으로 지정:

`mimetype --language {{경로/대상/파일}}`
