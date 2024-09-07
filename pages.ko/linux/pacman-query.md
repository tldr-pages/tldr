# pacman --query

> Arch Linux 패키지 관리 도구.
> 같이 보기: `pacman`.
> 더 많은 정보: <https://man.archlinux.org/man/pacman.8>.

- 설치된 패키지와 버전 나열:

`pacman --query`

- 명시적으로 설치된 패키지와 버전만 나열:

`pacman --query --explicit`

- 파일을 소유한 패키지 찾기:

`pacman --query --owns {{파일_이름}}`

- 설치된 패키지 정보 표시:

`pacman --query --info {{패키지}}`

- 패키지가 소유한 파일 나열:

`pacman --query --list {{패키지}}`

- 고아 패키지 나열 (의존성으로 설치되었지만 더 이상 어떤 패키지도 필요로 하지 않는 패키지):

`pacman --query --unrequired --deps --quiet`

- 저장소에서 찾을 수 없는 설치된 패키지 나열:

`pacman --query --foreign`

- 오래된 패키지 나열:

`pacman --query --upgrades`
