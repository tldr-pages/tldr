# smbget

> SMB 서버에서 파일을 다운로드하기 위한 `wget` 유사 도구.
> 더 많은 정보: <https://www.samba.org/samba/docs/current/man-html/smbget.1.html>.

- 서버에서 파일 다운로드:

`smbget {{smb://server/share/file}}`

- 공유 또는 폴더를 재귀적으로 다운로드:

`smbget --recursive {{smb://server/share}}`

- 사용자명과 비밀번호로 연결:

`smbget {{smb://server/share/file}} --user {{사용자명%비밀번호}}`

- 암호화된 전송 요구:

`smbget {{smb://server/share/file}} --encrypt`
