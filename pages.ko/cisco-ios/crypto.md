# crypto

> 암호화 관련 기능을 관리.
> 설정 모드에서 사용함.
> 더 많은 정보: <https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/crypto-is-cz-commands.html>.

- `rsa` 키 생성:

`crypto key generate rsa`

- 키의 modulus 값 지정하여 생성:

`crypto key generate rsa modulus {{1024}}`

- 모든 키 삭제:

`crypto key zeroize`
