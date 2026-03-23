# smbclient

> 서버의 SMB/CIFS 리소스에 접근하기 위한 FTP 유사 클라이언트.
> 더 많은 정보: <https://manned.org/smbclient>.

- 공유 서버에 연결(비밀번호 입력이 필요하며, `exit` 명령으로 세션 종료):

`smbclient {{//서버/공유}}`

- 다른 사용자명으로 연결:

`smbclient {{//서버/공유}} {{[-U|--user]}} {{사용자명}}`

- 다른 작업 그룹으로 연결:

`smbclient {{//서버/공유}} {{[-W|--workgroup]}} {{도메인}} {{[-U|--user]}} {{사용자명}}`

- 사용자명과 비밀번호로 연결:

`smbclient {{//서버/공유}} {{[-U|--user]}} {{사용자명%비밀번호}}`

- 서버에서 파일 다운로드:

`smbclient {{//서버/공유}} {{[-D|--directory]}} {{경로/대상/폴더}} {{[-c|--command]}} "get {{파일.txt}}"`

- 서버에 파일 업로드:

`smbclient {{//서버/공유}} {{[-D|--directory]}} {{경로/대상/폴더}} {{[-c|--command]}} "put {{파일.txt}}"`

- 서버의 공유 목록을 익명으로 나열:

`smbclient {{[-L|--list]}} {{서버}} --no-pass`
