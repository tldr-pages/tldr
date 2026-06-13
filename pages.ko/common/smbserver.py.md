# smbserver.py

> SMB 공유를 호스팅.
> Impacket 도구 모음의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- 기본 SMB 공유를 설정:

`smbserver.py {{공유이름}} {{경로/대상/공유파일}}`

- 사용자 지정 설명을 포함한 공유를 설정:

`smbserver.py -comment {{my_share}} {{공유이름}} {{경로/대상/공유파일}}`

- 사용자 이름과 비밀번호 인증을 사용하는 공유를 설정:

`smbserver.py -username {{username}} -password {{password}} {{공유이름}} {{경로/대상/공유파일}}`

- NTLM 해시 인증을 사용하는 공유를 설정:

`smbserver.py -hashes {{LMHASH}}:{{NTHASH}} {{공유이름}} {{경로/대상/공유파일}}`

- 특정 인터페이스에서 공유를 설정:

`smbserver.py {{[-ip|--interface-address]}} {{인터페이스_ip_주소}} {{공유이름}} {{경로/대상/공유파일}}`

- 표준이 아닌 SMB 포트에서 공유를 설정:

`smbserver.py -port {{포트}} {{공유이름}} {{경로/대상/공유파일}}`

- SMB2 지원을 활성화하여 공유를 설정:

`smbserver.py -smb2support {{공유이름}} {{경로/대상/공유파일}}`

- 공유를 설정하고 명령을 출력파일에 기록:

`smbserver.py -outputfile {{경로/대상/출력파일}} {{공유이름}} {{경로/대상/공유파일}}`
