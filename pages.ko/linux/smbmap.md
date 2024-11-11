# smbmap

> SMB 열거 도구.
> 더 많은 정보: <https://github.com/ShawnDEvans/smbmap>.

- 사용자의 비밀번호 또는 NTLM 해시를 입력하여 호스트의 SMB 공유 및 권한 표시:

`smbmap -u {{사용자명}} --prompt -H {{IP}}`

- 도메인을 지정하고 비밀번호 NTLM 해시를 입력하여 호스트의 SMB 공유 및 권한 표시:

`smbmap -u {{사용자명}} --prompt -d {{도메인}} -H {{IP}}`

- SMB 공유를 표시하고 단일 수준의 디렉토리 및 파일 나열:

`smbmap -u {{사용자명}} --prompt -H {{IP}} -r`

- SMB 공유를 표시하고 정의된 수준의 디렉토리 및 파일을 재귀적으로 나열:

`smbmap -u {{사용자명}} --prompt -H {{IP}} -R --depth {{3}}`

- SMB 공유를 표시하고 디렉토리 및 파일을 재귀적으로 나열하며, 정규 표현식과 일치하는 파일 다운로드:

`smbmap -u {{사용자명}} --prompt -H {{IP}} -R -A {{패턴}}`

- SMB 공유를 표시하고 디렉토리 및 파일을 재귀적으로 나열하며, 정규 표현식과 일치하는 파일 내용을 검색:

`smbmap -u {{사용자명}} --prompt -H {{IP}} -R -F {{패턴}}`

- 원격 시스템에서 셸 명령 실행:

`smbmap -u {{사용자명}} --prompt -H {{IP}} -x {{명령}}`

- 파일을 원격 시스템에 업로드:

`smbmap -u {{사용자명}} --prompt -H {{IP}} --upload {{소스}} {{대상}}`
