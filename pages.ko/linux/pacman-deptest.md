# pacman --deptest

> 지정된 각 의존성을 확인하고 시스템에 현재 충족되지 않은 의존성 목록을 반환합니다.
> 같이 보기: `pacman`.
> 더 많은 정보: <https://man.archlinux.org/man/pacman.8>.

- 설치되지 않은 의존성의 패키지 이름을 출력:

`pacman --deptest {{패키지1 패키지2 ...}}`

- 설치된 패키지가 주어진 최소 버전을 충족하는지 확인:

`pacman --deptest "{{bash>=5}}"`

- 패키지의 최신 버전이 설치되었는지 확인:

`pacman --deptest "{{bash>5}}"`

- 도움말 표시:

`pacman --deptest --help`
