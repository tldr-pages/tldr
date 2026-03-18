# smbclient.py

> SMB 서버와 상호작용.
> Impacket 도구 모음의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 사용자 이름과 비밀번호를 사용하여 SMB 서버에 연결:

`smbclient.py {{도메인}}/{{사용자명}}:{{비밀번호}}@{{target}}`

- NTLM 해시를 사용하여 인증을 연결:

`smbclient.py -hashes {{LM_HASH}}:{{NT_HASH}} {{도메인}}/{{사용자명}}@{{target}}`

- Kerberos 인증을 사용해 연결:

`smbclient.py -k {{도메인}}/{{사용자명}}@{{목표}}`

- 도메인 컨트롤러 IP를 지정하여 연결:

`smbclient.py -dc-ip {{도메인_컨트롤러_ip}} {{도메인}}/{{사용자명}}:{{비밀번호}}@{{목표}}`

- NetBIOS 이름 대신 특정 대상 IP를 지정하여 연결:

`smbclient.py -target-ip {{목표_ip}} {{도메인}}/{{사용자명}}:{{비밀번호}}@{{목표}}`

- 표준이 아닌 SMB 포트를 사용해 연결:

`smbclient.py -port {{포트}} {{도메인}}/{{사용자명}}:{{비밀번호}}@{{목표}}`

- SMB 셸에서 입력 파일의 명령을 실행:

`smbclient.py -inputfile {{경로/대상/입력_파일}} {{도메인}}/{{사용자명}}:{{비밀번호}}@{{목표}}`

- SMB 클라이언트 명령을 출력 파일에 기록:

`smbclient.py -outputfile {{경로/대상/출력_파일}} {{도메인}}/{{사용자명}}:{{비밀번호}}@{{목표}}`
