# hledger accounts

> 계정 이름을 나열.
> 더 많은 정보: <https://hledger.org/hledger.html#accounts>.

- 기본 저널 파일에서 사용되거나 선언된 모든 계정 표시:

`hledger {{[acc|accounts]}}`

- 트랜잭션에서 사용된 계정만 표시:

`hledger {{[acc|accounts]}} {{[-u|--used]}}`

- account 지시문으로 선언된 계정만 표시:

`hledger {{[acc|accounts]}} {{[-d|--declared]}}`

- 사용되었지만 선언되지 않은 계정에 대해 account 지시문을 생성하여 저널에 추가:

`hledger {{[acc|accounts]}} --undeclared --directives >> {{2024-accounts.journal}}`

- 이름에 `asset`이 포함된 계정과 해당 계정의 선언된/추론된 타입 표시:

`hledger {{[acc|accounts]}} asset --types`

- `Asset` 타입의 계정만 표시:

`hledger {{[acc|accounts]}} type:A`

- 계정 계층 구조의 처음 두 단계만 트리 형태로 표시:

`hledger {{[acc|accounts]}} {{[-t|--tree]}} {{[-2|--depth 2]}}`
