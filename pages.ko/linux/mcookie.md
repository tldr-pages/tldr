# mcookie

> 랜덤 128비트 16진수 숫자를 생성합니다.
> 더 많은 정보: <https://manned.org/mcookie>.

- 랜덤 숫자 생성:

`mcookie`

- 파일의 내용을 난수 생성의 시드로 사용하여 랜덤 숫자 생성:

`mcookie --file {{경로/대상/파일}}`

- 파일에서 특정 바이트 수를 난수 생성의 시드로 사용하여 랜덤 숫자 생성:

`mcookie --file {{경로/대상/파일}} --max-size {{바이트_수}}`

- 사용된 난수의 출처 및 시드와 같은 세부 정보를 출력:

`mcookie --verbose`
