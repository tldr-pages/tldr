# machine_role.py

> 원격 Windows 머신의 역할을 확인 (예:.도메인 컨트롤러, 멤버 서버, 워크스테이션).
> Impacket 도구 모음의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 사용자 이름과 비밀번호를 사용하여 머신 역할을 확인:

`machine_role.py {{도메인}}/{{사용자명}}:{{비밀번호}}@{{target}}`

- pass-the-hash 인증을 사용하여 머신 역할 확인:

`machine_role.py -hashes {{LM_Hash}}:{{NT_Hash}} {{도메인}}/{{사용자명}}@{{대상}}`

- 비밀번호 입력 없이 머신의 역할 확인 (예: 기존 인증 세션 사용):

`machine_role.py -no-pass {{도메인}}/{{사용자명}}@{{대상}}`

- Kerberos 인증을 사용하여 머신 역할을 확인:

`machine_role.py -k {{도메인}}/{{사용자명}}@{{대상}}`

- 도메인 컨트롤러의 IP 주소를 지정:

`machine_role.py -dc-ip {{ip_주소}} {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}}`
