# pacman --database

> Arch Linux 패키지 데이터베이스를 조작합니다.
> 설치된 패키지의 특정 속성을 수정합니다.
> 같이 보기: `pacman`.
> 더 많은 정보: <https://man.archlinux.org/man/pacman.8>.

- 패키지를 암묵적으로 설치된 것으로 표시:

`sudo pacman --database --asdeps {{패키지}}`

- 패키지를 명시적으로 설치된 것으로 표시:

`sudo pacman --database --asexplicit {{패키지}}`

- 모든 패키지 의존성이 설치되었는지 확인:

`pacman --database --check`

- 모든 지정된 의존성이 사용 가능한지 확인하기 위해 저장소 검사:

`pacman --database --check --check`

- 오류 메시지만 표시:

`pacman --database --check --quiet`

- 도움말 표시:

`pacman --database --help`
