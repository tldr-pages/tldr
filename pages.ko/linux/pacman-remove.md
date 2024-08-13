# pacman --remove

> Arch Linux 패키지 관리 도구.
> 같이 보기: `pacman`.
> 더 많은 정보: <https://man.archlinux.org/man/pacman.8>.

- 패키지와 그 의존성 제거:

`sudo pacman --remove --recursive {{패키지}}`

- 패키지와 그 의존성 및 구성 파일 제거:

`sudo pacman --remove --recursive --nosave {{패키지}}`

- 확인 없이 패키지 제거:

`sudo pacman --remove --noconfirm {{패키지}}`

- 고아 패키지 제거 (의존성으로 설치되었지만 더 이상 어떤 패키지도 필요로 하지 않는 패키지):

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- 패키지와 해당 패키지를 의존하는 모든 패키지 제거:

`sudo pacman --remove --cascade {{패키지}}`

- 영향을 받을 패키지 목록 표시 (패키지를 제거하지 않음):

`pacman --remove --print {{패키지}}`

- 도움말 표시:

`pacman --remove --help`
