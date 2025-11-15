# age-keygen

> `age` 키 쌍을 생성합니다.
> 더 보기: 파일을 암호화/복호화하기 위한 `age` 명령어.
> 더 많은 정보: <https://manned.org/age-keygen>.

- 키 쌍을 생성하고, 암호화되지 않은 파일에 저장한 후 공개키를 `stdout`에 인쇄:

`age-keygen --output {{경로/대상/파일}}`

- 인증 정보(identit[y])를 수신자로 변환하고, 공개 키를 `stdout`에 인쇄:

`age-keygen -y {{경로/대상/파일}}`
