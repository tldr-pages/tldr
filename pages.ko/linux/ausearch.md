# ausearch

> Linux audit 로그에서 이벤트를 조회하는 도구.
> `audit` 패키지의 일붘.
> 관련 항목: `audit2why`, `audit2allow`, `aureport`.
> 더 많은 정보: <https://manned.org/ausearch>.

- 모든 SELinux AVC 거부 이벤트 검색:

`sudo ausearch {{[-m|--message]}} avc`

- 특정 실행 파일과 관련된 이벤트 검색:

`sudo ausearch {{[-c|--comm]}} {{httpd}}`

- 특정 사용자 이벤트 검색:

`sudo ausearch {{[-ui|--uid]}} {{1000}}`

- 최근 10분 내 이벤트 검색:

`sudo ausearch {{[-ts|--start]}} recent`

- 로그인 실패 이벤트 검색:

`sudo ausearch {{[-m|--message]}} user_login {{[-sv|--success]}} no`

- 특정 파일 관련 이벤트 검색:

`sudo ausearch {{[-f|--file]}} {{경로/대상/파일}}`

- 후처리를 위해 raw 형식으로 결과 출력:

`sudo ausearch {{[-m|--message]}} avc --raw`
