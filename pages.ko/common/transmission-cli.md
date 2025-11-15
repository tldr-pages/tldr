# transmission-cli

> 경량의 명령줄 기반 BitTorrent 클라이언트.
> 이 도구는 사용이 중단되었습니다. `transmission-remote`를 참조하세요.
> 더 많은 정보: <https://manned.org/transmission-cli>.

- 특정 토렌트 다운로드:

`transmission-cli {{url|마그넷|경로/대상/파일}}`

- 특정 디렉토리에 토렌트 다운로드:

`transmission-cli {{[-w|--download-dir]}} {{경로/대상/다운로드_디렉토리}} {{url|마그넷|경로/대상/파일}}`

- 특정 파일이나 디렉토리에서 토렌트 파일 생성:

`transmission-cli --new {{경로/대상/소스_파일_또는_디렉토리}}`

- 다운로드 속도 제한 설정 (KB/s 단위):

`transmission-cli {{[-d|--downlimit]}} {{50}} {{url|마그넷|경로/대상/파일}}`

- 업로드 속도 제한 설정 (KB/s 단위):

`transmission-cli {{[-u|--uplimit]}} {{50}} {{url|마그넷|경로/대상/파일}}`

- 특정 포트를 사용하여 연결:

`transmission-cli {{[-p|--port]}} {{포트_번호}} {{url|마그넷|경로/대상/파일}}`

- 피어 연결에 암호화 강제 적용:

`transmission-cli {{[-er|--encryption-required]}} {{url|마그넷|경로/대상/파일}}`

- Bluetack 형식의 피어 차단 목록 사용:

`transmission-cli {{[-b|--blocklist]}} {{차단목록_url|경로/대상/차단목록}} {{url|마그넷|경로/대상/파일}}`
