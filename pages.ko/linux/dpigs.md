# dpigs

> `apt` 기반 시스템에서 설치된 패키지 중 가장 많은 공간을 차지하는 패키지를 표시합니다.
> 더 많은 정보: <https://manned.org/dpigs>.

- 시스템에서 가장 큰 N개의 패키지 표시:

`dpigs --lines={{N}}`

- 기본 dpkg [s]tatus 파일 대신 지정된 [f]파일 사용:

`dpigs --status={{경로/대상/파일}}`

- 시스템에 설치된 바이너리 패키지의 가장 큰 [S]소스 패키지 표시:

`dpigs --source`

- 패키지 크기를 사람이 읽기 쉬운 [H]형식으로 표시:

`dpigs --human-readable`

- 도움말 표시:

`dpigs --help`
