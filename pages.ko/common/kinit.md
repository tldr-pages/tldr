# kinit

> Kerberos 서버와 주체를 인증하여 티켓을 얻고 캐시.
> 참고: Kerberos 주체는 사용자, 서비스 또는 애플리케이션일 수 있습니다.
> 더 많은 정보: <https://web.mit.edu/kerberos/krb5-latest/doc/user/user_commands/kinit.html>.

- 사용자를 인증하고 티켓 발급 티켓 획득:

`kinit {{사용자명}}`

- 티켓 발급 티켓 갱신:

`kinit -R`

- 티켓의 유효 기간 지정:

`kinit -l {{5시간}}`

- 티켓의 총 갱신 가능 기간 지정:

`kinit -r {{1주}}`

- 다른 주체 이름으로 인증 지정:

`kinit -p {{주체@REALM}}`

- 다른 키탭 파일로 인증 지정:

`kinit -t {{경로/대상/keytab}}`
