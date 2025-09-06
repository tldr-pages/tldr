# gmssl

> GmSSL은 SM1, SM2, SM3, SM4, SM9 및 ZUC/ZUC256을 지원하는 암호화 툴킷.
> 더 많은 정보: <http://gmssl.org/english.html>.

- 파일에 대한 SM3 해시를 생성:

`gmssl sm3 {{경로/대상/파일}}`

- SM4 암호를 사용하여 파일을 암호화:

`gmssl sms4 -e -in {{경로/대상/파일}} -out {{경로/대상/파일.sms4}}`

- SM4 암호를 사용하여 파일을 복호화:

`gmssl sms4 -d -in {{경로/대상/파일.sms4}}`

- SM2 개인키를 생성:

`gmssl sm2 -genkey -out {{경로/대상/파일.pem}}`

- 기존 개인 키에서 SM2 공개키를 생성:

`gmssl sm2 -pubout -in {{경로/대상/파일.pem}} -out {{경로/대상/파일.pem.pub}}`

- ZUC 암호를 사용하여 파일을 암호화:

`gmssl zuc -e -in {{경로/대상/파일}} -out {{경로/대상/파일.zuc}}`

- ZUC 암호를 사용하여 파일을 복호화:

`gmssl zuc -d -in {{경로/대상/파일.zuc}}`

- 버전 정보 출력:

`gmssl version`
