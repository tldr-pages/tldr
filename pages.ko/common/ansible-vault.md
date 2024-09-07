# ansible-vault

> Ansible 프로젝트 내에서 값, 데이터 구조 및 파일을 암호화하고 해독.
> 더 많은 정보: <https://docs.ansible.com/ansible/latest/user_guide/vault.html#id17>.

- 비밀번호를 입력하라는 메시지가 표시된 새로운 암호화된 볼트 파일을 만듬:

`ansible-vault create {{볼트_파일}}`

- 볼트 키 파일을 사용하여, 암호화된 새 볼트 파일을 만듬:

`ansible-vault create --vault-password-file {{비밀번호_파일}} {{볼트_파일}}`

- 선택적 비밀번호 파일을 사용하여, 기존 파일을 암호화:

`ansible-vault encrypt --vault-password-file {{비밀번호_파일}} {{볼트_파일}}`

- Ansible의 암호화된 문자열 형식을 사용하여, 문자열을 암호화하고 대화형 프롬프트를 표시:

`ansible-vault encrypt_string`

- 암호 파일을 사용하여, 암호화된 파일을 해독하는 방법:

`ansible-vault view --vault-password-file {{비밀번호_파일}} {{볼트_파일}}`

- 이미 암호화된 볼트 파일을 새 암호 파일로 다시 키 지정:

`ansible-vault rekey --vault-password-file {{예전_비밀번호_파일}} --new-vault-password-file {{새로운_비밀번호_파일}} {{볼트_파일}}`
