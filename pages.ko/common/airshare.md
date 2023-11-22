# airshare

> 로컬 네트워크의 두 컴퓨터 사이의 데이터 전송.
> 더 많은 정보: <https://airshare.rtfd.io/en/latest/cli.html>.

- 파일 또는 디렉터리 공유:

`airshare {{코드}} {{경로/대상/파일_또는_디렉토리1 경로/대상/파일_또는_디렉토리2 ...}}`

- 파일 받기:

`airshare {{코드}}`

- 수신 서버 호스팅 (웹 인터페이스를 사용하여 파일을 업로드할 때 사용):

`airshare --upload {{코드}}`

- 파일이나 디렉터리를 수신 서버로 전송:

`airshare --upload {{코드}} {{경로/대상/파일_또는_디렉토리1 경로/대상/파일_또는_디렉토리2 ...}}`

- 경로가 클립보드에 복사된 파일 전송:

`airshare --file-path {{코드}}`

- 파일을 받아 클립보드에 복사:

`airshare --clip-receive {{코드}}`
