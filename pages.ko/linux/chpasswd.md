# chpasswd

> 여러 사용자의 비밀번호를 `stdin`을 통해 변경합니다.
> 더 많은 정보: <https://manned.org/chpasswd.8>.

- 특정 사용자의 비밀번호 변경:

`printf "{{사용자명}}:{{새_비밀번호}}" | sudo chpasswd`

- 여러 사용자의 비밀번호 변경 (입력 텍스트에는 공백이 없어야 합니다.):

`printf "{{사용자명_1}}:{{새_비밀번호_1}}\n{{사용자명_2}}:{{새_비밀번호_2}}" | sudo chpasswd`

- 특정 사용자의 비밀번호를 암호화된 형태로 변경:

`printf "{{사용자명}}:{{새_암호화된_비밀번호}}" | sudo chpasswd --encrypted`

- 특정 사용자의 비밀번호를 변경하고 저장된 비밀번호에 특정 암호화를 사용:

`printf "{{사용자명}}:{{새_비밀번호}}" | sudo chpasswd --crypt-method {{NONE|DES|MD5|SHA256|SHA512}}`
