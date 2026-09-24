# kioclient

> KDE의 KIO 서브시스템을 사용하여 네트워크 투명 파일 작업 수행.
> `file:`, `sftp:`, `smb:`, `fish:`, `trash:`와 같은 URL 스킴 지원.
> 더 많은 정보: <https://manned.org/kioclient>.

- URL을 기본 KDE 핸들러로 열기:

`kioclient exec {{주소}}`

- 원격 파일의 내용을 `stdout`으로 출력:

`kioclient cat {{sftp://user@host/경로/대상/파일}}`

- 원격 디렉터리의 내용 목록 표시:

`kioclient ls {{smb://server/share}}`

- KIO를 사용하여 하나 이상의 파일 복사:

`kioclient cp {{경로/대상/소스1 경로/대상/소스2 ...}} {{경로/대상/목적지}}`

- KIO를 사용하여 파일 이동:

`kioclient mv {{경로/대상/소스}} {{경로/대상/목적지}}`

- KIO를 사용하여 파일 삭제:

`kioclient rm {{주소}}`

- KIO를 사용하여 새로운 디렉터리 생성:

`kioclient mkdir {{주소}}`

- 도움말 표시:

`kioclient --help`
