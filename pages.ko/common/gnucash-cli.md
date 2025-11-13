# gnucash-cli

> GnuCash의 명령줄 버전.
> 더 많은 정보: <https://gnucash.org/viewdoc.phtml?rev=5&lang=C&doc=help>.

- 파일에 지정된 통화 및 주식에 대한 견적을 받아 출력:

`gnucash-cli --quotes get {{경로/대상/파일.gnucash}}`

- `--name`으로 지정된 특정 유형의 재무 보고서를 생성:

`gnucash-cli --report run --name "{{Balance Sheet}}" {{경로/대상/파일.gnucash}}`
