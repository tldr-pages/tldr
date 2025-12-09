# lpass

> LastPass 비밀번호 관리자의 명령줄 인터페이스.
> 더 많은 정보: <https://lastpass.github.io/lastpass-cli/lpass.1.html>.

- 마스터 비밀번호를 입력하여 LastPass 계정에 로그인:

`lpass login {{사용자이름}}`

- 로그인 상태 표시:

`lpass status`

- 카테고리별로 그룹화된 모든 사이트 나열:

`lpass ls`

- `myinbox` 식별자로 gmail.com의 새 비밀번호 생성 및 LastPass에 추가:

`lpass generate --username {{사용자이름}} --url {{gmail.com}} {{myinbox}} {{비밀번호_길이}}`

- 지정된 항목의 비밀번호 표시:

`lpass show {{myinbox}} --password`
