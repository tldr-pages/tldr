# dolos

> 프로그래밍 과제 표절을 탐지.
> 더 많은 정보: <https://dolos.ugent.be/docs/running.html>.

- 기본 분석 실행:

`dolos run {{경로/대상/파일/*}}`

- 웹 서버 화면과 함께 분석 실행:

`dolos run {{[-f|--output-format]}} web {{경로/대상/파일/*}}`

- 프로그래밍 언어를 지정하여 분석 실행:

`dolos run {{[-l|--language]}} {{언어_이름}} {{경로/대상/파일/*}}`

- 상용구/템플릿 코드를 제외하고 분석:

`dolos run {{[-i|--ignore]}} {{경로/대상/템플릿_파일}} {{경로/대상/파일/*}}`

- 분석 결과를 CSV 형식으로 출력:

`dolos run {{[-f|--output-format]}} csv {{경로/대상/파일/*}}`

- 기존 분석 보고서를 웹 서버로 제공:

`dolos serve {{경로/대상/보고서_디렉터리}}`

- 도움말 표시:

`dolos {{[-h|--help]}}`

- 버전 정보 표시:

`dolos {{[-v|--version]}}`
