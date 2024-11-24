# aptitude

> Debian 및 Ubuntu 패키지 관리 도구.
> 더 많은 정보: <https://manned.org/aptitude.8>.

- 사용 가능한 패키지 및 버전 목록 동기화. 이 명령은 다른 `aptitude` 명령을 실행하기 전에 먼저 실행해야 합니다:

`aptitude update`

- 새 패키지 및 그 의존성 설치:

`aptitude install {{패키지}}`

- 패키지 검색:

`aptitude search {{패키지}}`

- 설치된 패키지 검색 (`?installed`는 `aptitude` 검색 용어입니다):

`aptitude search '?installed({{패키지}})'`

- 특정 패키지 및 해당 패키지에 의존하는 모든 패키지 제거:

`aptitude remove {{패키지}}`

- 설치된 패키지를 가장 최신 버전으로 업그레이드:

`aptitude upgrade`

- 설치된 패키지 업그레이드 (`aptitude upgrade`와 유사)하며, 불필요한 패키지를 제거하고 새로운 패키지 의존성을 충족하기 위해 추가 패키지 설치:

`aptitude full-upgrade`

- 자동 업그레이드되지 않도록 설치된 패키지를 보류:

`aptitude hold '?installed({{패키지}})'`
