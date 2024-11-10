# hledger

> 강력하고 사용하기 쉬운 텍스트 기반 회계 앱.
> 같이 보기: TUI를 위한 `hledger-ui`, 웹 인터페이스를 위한 `hledger-web`.
> 더 많은 정보: <https://hledger.org/hledger.html>.

- 새로운 거래를 대화형으로 기록하고 기본 저널 파일에 저장:

`hledger add`

- `bank.csv`에서 새로운 거래를 가져오고, `bank.csv.rules`를 사용하여 변환:

`hledger import {{경로/대상/bank.csv}}`

- 여러 지정된 저널 파일에서 모든 거래를 출력:

`hledger print --file {{경로/대상/prices-2024.journal}} --file {{경로/대상/prices-2023.journal}}`

- 계정과 그 유형을 계층 구조로 모두 표시:

`hledger accounts --tree --types`

- 자산 및 부채 계정 잔액을 0을 포함하여 계층적으로 표시:

`hledger balancesheet --empty --tree --no-elide`

- 월별 수입/지출/총액을 가장 큰 것부터 2단계로 요약하여 표시:

`hledger incomestatement --monthly --row-total --average --sort --depth 2`

- `assets:bank:checking` 계정의 거래 및 진행 중인 잔액을 표시:

`hledger aregister assets:bank:checking`

- `assets:cash` 계정에서 음식에 소비한 금액을 표시:

`hledger print assets:cash | hledger -f- -I aregister expenses:food`
