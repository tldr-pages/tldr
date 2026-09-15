# ng extract-i18n

> 소스 코드에서 국제화(i18n) 메시지 추출.
> 더 많은 정보: <https://angular.dev/cli/extract-i18n>.

- i18n 메시지 추출:

`ng extract-i18n`

- 특정 형식으로 i18n 메시지 추출:

`ng extract-i18n --format {{arb|json|xlf|...}}`

- 특정 형식으로 i18n 메시지를 파일로 출력:

`ng extract-i18n --out-file {{경로/대상/파일}}`

- Extract i18n 메시지를 특정 디렉터리에 출력:

`ng extract-i18n --output-path {{경로/대상/디렉터리}}`

- 중복 번역 처리 방식 지정:

`ng extract-i18n --i18n-duplicate-translation {{에러|무시|경고}}`

- 진행 상황 출력:

`ng extract-i18n --progress`
