# hledger aregister

> 한 계좌의 거래 내역과 잔액을 한 줄로 표시.
> 더 많은 정보: <https://hledger.org/hledger.html#aregister>.

- `assets:bank:checking` 계좌의 거래 내역과 잔액 표시:

`hledger aregister assets:bank:checking`

- `*savings*`라는 이름의 첫 번째 계좌의 거래 내역과 잔액 표시:

`hledger aregister savings`

- 지정된 너비로 체크 계좌의 정리된 거래 내역 표시:

`hledger aregister checking --cleared --width {{120}}`

- 예측 규칙의 거래를 포함하여 체크 계좌의 내역 표시:

`hledger aregister checking --forecast`
