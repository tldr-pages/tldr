# ansible-vault

> Ansible 프로젝트에서 값, 데이터 구조, 파일을 암호화 및 복호화하는 도구.
> 더 많은 정보: <https://docs.ansible.com/projects/ansible/latest/vault_guide/index.html>.

- 비밀번호 입력을 통해 새로운 암호화된 vault 파일 생성:

`ansible-vault create {{경로/대상/vault_파일}}`

- 기존 암호화된 vault 파일을 비밀번호 입력으로 수정, 조회 또는 재암호화:

`ansible-vault {{edit|view|rekey}} {{경로/대상/vault_파일}}`

- 비밀번호 파일을 사용하여 새로운 암호화된 vault 파일 생성:

`ansible-vault create --vault-password-file {{경로/대상/비밀번호_파일}} {{경로/대상/vault_파일}}`

- 비밀번호 파일을 사용하여 기존 평문 파일을 제자리에서 암호화:

`ansible-vault encrypt --vault-password-file {{경로/대상/비밀번호_파일}} {{경로/대상/파일}}`

- Ansible의 암호화 문자열 형식으로 문자열 암호화 (대화형 입력 방식):

`ansible-vault encrypt_string`

- 비밀번호 파일을 사용하여 암호화된 vault 파일 조회:

`ansible-vault view --vault-password-file {{경로/대상/비밀번호_파일}} {{경로/대상/vault_파일}}`

- 기존 암호화된 vault 파일을 새로운 비밀번호 파일로 재암호화(re-encrypt):

`ansible-vault rekey --vault-password-file {{경로/대상/오래된_비밀번호_파일}} --new-vault-password-file {{경로/대상/새로운_비밀번호_파일}} {{경로/대상/vault_파일}}`
