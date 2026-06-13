# nxc smb

> SMB 서버를 침투 테스트하고 익스플로잇.
> 더 많은 정보: <https://www.netexec.wiki/smb-protocol/generate-hosts-file>.

- 지정된 [u]사용자명 및 [p]비밀번호 목록의 모든 조합을 시도하여 유효한 도메인 자격 증명 검색:

`nxc smb {{192.168.178.2}} {{[-u|--username]}} {{경로/대상/사용자명목록.txt}} {{[-p|--password]}} {{경로/대상/비밀번호목록.txt}}`

- 도메인 계정 대신 로컬 계정에 대한 유효한 자격 증명 검색:

`nxc smb {{192.168.178.2}} {{[-u|--username]}} {{경로/대상/사용자명목록.txt}} {{[-p|--password]}} {{경로/대상/비밀번호목록.txt}} --local-auth`

- 대상 호스트에서 SMB 공유 및 지정된 사용자의 액세스 권한 열거:

`nxc smb {{192.168.178.0/24}} {{[-u|--username]}} {{사용자명}} {{[-p|--password]}} {{비밀번호}} --shares`

- 패스-더-해시 인증을 통해 대상 호스트의 네트워크 인터페이스 열거:

`nxc smb {{192.168.178.30-45}} {{[-u|--username]}} {{사용자명}} {{[-H|--hash]}} {{NTLM_해시}} --interfaces`

- 대상 호스트에서 일반적인 취약점 스캔:

`nxc smb {{경로/대상/target_list.txt}} {{[-u|--username]}} '' {{[-p|--password]}} '' {{[-M|--module]}} zerologon {{[-M|--module]}} petitpotam`

- 대상 호스트에서 명령 실행 시도:

`nxc smb {{192.168.178.2}} {{[-u|--username]}} {{사용자명}} {{[-p|--password]}} {{비밀번호}} -x {{명령}}`
