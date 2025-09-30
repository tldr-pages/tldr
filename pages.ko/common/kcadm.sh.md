# kcadm.sh

> 관리 작업 수행.
> 더 많은 정보: <https://www.keycloak.org/docs/latest/server_admin/#admin-cli>.

- 인증된 세션 시작:

`kcadm.sh config credentials --server {{호스트}} --realm {{영역_이름}} --user {{사용자명}} --password {{비밀번호}}`

- 사용자 생성:

`kcadm.sh create users -s username={{사용자명}} -r {{영역_이름}}`

- 모든 영역 나열:

`kcadm.sh get realms`

- JSON 구성으로 영역 업데이트:

`kcadm.sh update realms/{{영역_이름}} -f {{경로/대상/파일.json}}`
