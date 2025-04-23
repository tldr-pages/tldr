# chpass

> 로그인 셸과 비밀번호를 포함한 사용자 데이터베이스 정보를 추가하거나 변경합니다.
> 같이 보기: `passwd`.
> 더 많은 정보: <https://man.openbsd.org/chpass>.

- 현재 사용자에게 특정 로그인 셸을 대화식으로 설정:

`doas chpass`

- 현재 사용자에게 특정 로그인 셸을 설정:

`doas chpass -s {{경로/대상/셸}}`

- 특정 사용자에게 로그인 셸을 설정:

`doas chpass -s {{경로/대상/셸}} {{사용자명}}`

- `passwd` 파일 형식의 사용자 데이터베이스 항목을 지정:

`doas chpass -a {{사용자명:암호화된_비밀번호:uid:gid:...}}`
