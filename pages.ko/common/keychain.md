# keychain

> ssh-agent 및/또는 gpg-agent를 로그인 간에 재사용.
> 더 많은 정보: <https://funtoo.org/Keychain>.

- 실행 중인 ssh-agent를 확인하고 필요한 경우 시작:

`keychain`

- gpg-agent도 확인:

`keychain --agents "{{gpg,ssh}}"`

- 모든 활성 키의 서명 나열:

`keychain --list`

- 모든 활성 키의 지문 나열:

`keychain --list-fp`

- 에이전트에 추가된 ID에 대한 타임아웃을 분 단위로 추가:

`keychain --timeout {{분}}`
