# hledger-ui

> `hledger`의 터미널 인터페이스(TUI), 강력하고 친숙한 일반 텍스트 회계 앱.
> 더 많은 정보: <https://hledger.org/hledger-ui.html>.

- 기본 저널 파일을 읽어 메인 메뉴 화면에서 시작:

`hledger-ui`

- 다른 색상 테마로 시작:

`hledger-ui --theme {{terminal|greenterm|dark}}`

- 대차대조표 계정 화면에서 시작하고, 계층 구조를 3단계까지 표시:

`hledger-ui --bs --tree --depth 3`

- 이 계정의 화면에서 시작하고, 정리된 거래를 표시하며 변경 시 다시 로드:

`hledger-ui --register {{assets:bank:checking}} --cleared --watch`

- 두 개의 저널 파일을 읽고, 알려진 경우 현재 가치로 금액을 표시:

`hledger-ui --file {{경로/대상/2024.journal}} --file {{경로/대상/2024-prices.journal}} --value now`

- 가능한 경우 Info 형식으로 매뉴얼 표시:

`hledger-ui --info`

- 도움말 표시:

`hledger-ui --help`
