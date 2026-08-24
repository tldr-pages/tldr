# hurl

> 간단한 텍스트 형식으로 정의된 HTTP 요청을 실행하고 테스트하는 도구.
> 내부적으로 `curl`을 기반으로 동작.
> 더 많은 정보: <https://hurl.dev/docs/manual.html>.

- 파일에 정의된 HTTP 요청 실행:

`hurl {{경로/대상/파일.hurl}}`

- 변수를 설정하여 HTTP 요청 실행:

`hurl --variable {{변수_이름}}={{값}} {{경로/대상/파일.hurl}}`

- 로그 및 리포트에서 마스킹될 비밀값을 설정하여 HTTP 요청 실행:

`hurl --secret {{비밀_이름}}={{값}} {{경로/대상/파일.hurl}}`

- 파일에서 변수와 비밀값을 불러와 HTTP 요청 실행:

`hurl --variables-file {{경로/대상/변수_파일}} --secrets-file {{경로/대상/시크릿_파일}} {{경로/대상/파일.hurl}}`

- 파일 내 특정 범위의 HTTP 요청만 실행(예: 2번부터 5번까지):

`hurl --from-entry 2 --to-entry 5 {{경로/대상/파일.hurl}}`

- 파일로부터 HTTP 요청 테스트를 실행하고 HTML 리포트를 생성:

`hurl --test --report-html {{경로/대상/출력_디렉터리}} {{경로/대상/파일.hurl}}`
