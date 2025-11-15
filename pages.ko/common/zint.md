# zint

> 바코드 및 QR 코드를 생성.
> 더 많은 정보: <https://www.zint.org.uk/manual/chapter/4>.

- 바코드를 생성하고 저장:

`zint --data "{{UTF-8 데이터}}" --output {{경로/대상/파일}}`

- 생성할 코드 유형 지정:

`zint --barcode {{코드_유형}} --data "{{UTF-8 데이터}}" --output {{경로/대상/파일}}`

- 지원되는 모든 코드 유형 나열:

`zint --types`
