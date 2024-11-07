# debchange

> Debian 소스 패키지의 debian/changelog 파일을 관리합니다.
> 더 많은 정보: <https://manned.org/debchange.1>.

- 비관리자 업로드를 위한 새 버전을 변경 로그에 추가:

`debchange --nmu`

- 현재 버전에 변경 로그 항목 추가:

`debchange --append`

- 지정된 ID의 버그를 종료하는 변경 로그 항목 추가:

`debchange --closes {{버그_ID}}`
