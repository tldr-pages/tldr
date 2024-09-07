# pacman --files

> Arch Linux 패키지 관리 도구.
> 같이 보기: `pacman`, `pkgfile`.
> 더 많은 정보: <https://man.archlinux.org/man/pacman.8>.

- 패키지 데이터베이스 업데이트:

`sudo pacman --files --refresh`

- 특정 파일을 소유한 패키지 찾기:

`pacman --files {{파일_이름}}`

- 정규 표현식을 사용하여 특정 파일을 소유한 패키지 찾기:

`pacman --files --regex '{{정규표현식}}'`

- 패키지 이름만 나열:

`pacman --files --quiet {{파일_이름}}`

- 특정 패키지가 소유한 파일 나열:

`pacman --files --list {{패키지}}`

- 도움말 표시:

`pacman --files --help`
