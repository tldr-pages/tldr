# mokutil

> Secure Boot Machine Owner Keys (MOK)를 구성.
> Secure Boot 활성화/비활성화 또는 키 등록과 같은 일부 작업은 재부팅이 필요합니다.
> 더 많은 정보: <https://manned.org/mokutil>.

- Secure Boot가 활성화되어 있는지 표시:

`mokutil --sb-state`

- Secure Boot 활성화:

`mokutil --enable-validation`

- Secure Boot 비활성화:

`mokutil --disable-validation`

- 등록된 키 나열:

`mokutil --list-enrolled`

- 새 키 등록:

`mokutil --import {{경로/대상/키.der}}`

- 등록될 키 나열:

`mokutil --list-new`

- shim 자세히 설정:

`mokutil --set-verbosity true`
