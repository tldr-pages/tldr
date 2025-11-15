# upt

> 다양한 운영 체제에서 패키지를 관리하기 위한 통합 인터페이스로, Windows, 여러 Linux 배포판, macOS, FreeBSD, Haiku 등을 지원합니다.
> 기본 OS 패키지 관리자가 설치되어 있어야 합니다.
> 같이 보기: `flatpak`, `brew`, `scoop`, `apt`, `dnf`.
> 더 많은 정보: <https://github.com/sigoden/upt>.

- 사용 가능한 패키지 목록 업데이트:

`upt update`

- 특정 패키지 검색:

`upt search {{검색_어구}}`

- 패키지에 대한 정보 표시:

`upt info {{패키지}}`

- 특정 패키지 설치:

`upt install {{패키지}}`

- 특정 패키지 제거:

`upt {{remove|uninstall}} {{패키지}}`

- 설치된 모든 패키지 업그레이드:

`upt upgrade`

- 특정 패키지 업그레이드:

`upt upgrade {{패키지}}`

- 설치된 패키지 목록 나열:

`upt list`
