# ledger

> 강력한 복식부기 회계 시스템.
> 더 많은 정보: <https://www.ledger-cli.org>.

- 총계를 보여주는 잔액 보고서 출력:

`ledger balance --file {{경로/대상/ledger.journal}}`

- 금액순으로 정렬된 지출 내역의 모든 게시물 나열:

`ledger register {{지출}} --sorted {{금액}}`

- 음료 및 음식 이외의 총 지출 출력:

`ledger balance {{지출}} and not ({{음료}} or {{음식}})`

- 예산 보고서 출력:

`ledger budget`

- 모든 게시물에 대한 요약 정보 출력:

`ledger stats`
