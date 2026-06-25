# GetADUsers.py

> Active Directory 사용자 목록과 마지막 로그인 시간, 이메일 등의 속성 조회.
> Impacket 도구 모음의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 모든 Active Directory 사용자 및 속성 열거:

`GetADUsers.py -all -dc-ip {{도메인_컨트롤러_ip}} {{도메인}}/{{사용자명}}:{{비밀번호}}`

- 특정 사용자 정보만 조회:

`GetADUsers.py -user {{사용자}} -dc-ip {{도메인_컨트롤러_ip}} {{도메인}}/{{사용자명}}:{{비밀번호}}`

- pass-the-hash 인증을 사용하여 사용자 정보 추출:

`GetADUsers.py -all -dc-ip {{도메인_컨트롤러_ip}} -hashes {{LM_Hash}}:{{NT_Hash}} {{도메인}}/{{사용자명}}`

- 결과를 파일로 저장:

`GetADUsers.py -all -dc-ip {{도메인_컨트롤러_ip}} {{도메인}}/{{사용자명}}:{{비밀번호}} > {{경로/대상/출력파일.txt}}`
