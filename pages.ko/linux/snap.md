# snap

> "snap" 독립형 소프트웨어 패키지 관리.
> `.deb` 파일에 대한 `apt`와 유사.
> 더 많은 정보: <https://manned.org/snap>.

- 패키지 검색:

`snap find {{검색어}}`

- 패키지 설치:

`snap install {{패키지}}`

- 패키지 업데이트:

`snap refresh {{패키지}}`

- 패키지를 다른 채널(트랙, 위험도, 브랜치)로 업데이트:

`snap refresh {{패키지}} --channel={{채널}}`

- 모든 패키지 업데이트:

`snap refresh`

- 설치된 snap 소프트웨어의 기본 정보 표시:

`snap list`

- 패키지 제거:

`snap remove {{패키지}}`

- 시스템의 최근 snap 변경 사항 확인:

`snap changes`
