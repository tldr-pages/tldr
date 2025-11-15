# nologin

> 사용자가 로그인하지 못하도록 하는 대체 셸.
> 더 많은 정보: <https://manned.org/nologin.5>.

- 사용자의 로그인 셸을 `nologin`으로 설정하여 로그인을 방지:

`chsh -s {{사용자}} nologin`

- `nologin` 로그인 셸을 가진 사용자에게 표시할 메시지 사용자 지정:

`echo "{{로그인_거부_메시지}}" > /etc/nologin.txt`
