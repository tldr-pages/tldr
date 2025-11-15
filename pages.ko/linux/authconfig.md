# authconfig

> 시스템 인증 리소스를 구성합니다.
> 더 많은 정보: <https://manned.org/authconfig>.

- 현재 설정 표시(또는 드라이 런):

`authconfig --test`

- 서버가 다른 비밀번호 해싱 알고리즘을 사용하도록 구성:

`authconfig --update --passalgo={{알고리즘}}`

- LDAP 인증 활성화:

`authconfig --update --enableldapauth`

- LDAP 인증 비활성화:

`authconfig --update --disableldapauth`

- 네트워크 정보 서비스 (NIS) 활성화:

`authconfig --update --enablenis`

- Kerberos 활성화:

`authconfig --update --enablekrb5`

- Winbind (액티브 디렉토리) 인증 활성화:

`authconfig --update --enablewinbindauth`

- 로컬 권한 부여 활성화:

`authconfig --update --enablelocauthorize`
