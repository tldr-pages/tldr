# dropbearkey

> Dropbear 형식으로 SSH 키를 생성합니다.
> 더 많은 정보: <https://manned.org/dropbearkey>.

- [t]유형 ed25519의 SSH 키를 생성하여 키 [f]파일에 저장:

`dropbearkey -t {{ed25519}} -f {{경로/대상/키_파일}}`

- [t]유형 ecdsa의 SSH 키를 생성하여 키 [f]파일에 저장:

`dropbearkey -t {{ecdsa}} -f {{경로/대상/키_파일}}`

- 4096비트 키 [s]크기의 [t]유형 RSA SSH 키를 생성하여 키 [f]파일에 저장:

`dropbearkey -t {{rsa}} -s {{4096}} -f {{경로/대상/키_파일}}`

- 키 [f]파일의 개인 키 지문과 공개 키 출력:

`dropbearkey -y -f {{경로/대상/키_파일}}`
