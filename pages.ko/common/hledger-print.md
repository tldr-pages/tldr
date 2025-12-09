# hledger print

> 전체 저널 항목을 표시하여 거래를 나타냅니다.
> 더 많은 정보: <https://hledger.org/hledger.html#print>.

- 기본 저널 파일의 모든 거래 표시:

`hledger print`

- 암시된 금액이나 비용을 명시적으로 하여 거래 표시:

`hledger print --explicit --infer-costs`

- 두 개의 지정된 파일에서 거래를 표시하고, 금액을 비용으로 변환:

`hledger print --file {{경로/대상/2023.journal}} --file {{경로/대상/2024.journal}} --cost`

- 이번 달 `*food*` 계좌의 `$` 거래를 표시하되, `*groceries*` 계좌는 제외:

`hledger print cur:\\$ food not:groceries date:thismonth`

- 설명에 `whole foods`가 포함된 50 이상의 금액 거래 표시:

`hledger print amt:'>50' desc:'whole foods'`

- `EUR` 금액을 소수점 콤마로 반올림하여 입금된 거래 표시:

`hledger print --cleared --commodity '1000, EUR' --round hard`

- `foo.journal`의 거래를 CSV 파일로 작성:

`hledger print --file {{경로/대상/foo.journal}} --output-file {{경로/대상/output_file.csv}}`
