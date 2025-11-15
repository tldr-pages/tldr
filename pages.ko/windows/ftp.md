# ftp

> 로컬 및 원격 FTP 서버 간에 파일을 상호작용하며 전송.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftp>.

- 원격 FTP 서버에 상호작용하며 연결:

`ftp {{호스트}}`

- 익명 사용자로 로그인:

`ftp -A {{호스트}}`

- 초기 연결 시 자동 로그인 비활성화:

`ftp -n {{호스트}}`

- FTP 명령 목록이 포함된 파일 실행:

`ftp -s:{{경로\대상\파일}} {{호스트}}`

- 여러 파일 다운로드(글롭 표현식):

`mget {{*.png}}`

- 여러 파일 업로드(글롭 표현식):

`mput {{*.zip}}`

- 원격 서버에서 여러 파일 삭제:

`mdelete {{*.txt}}`

- 도움말 표시:

`ftp --help`
