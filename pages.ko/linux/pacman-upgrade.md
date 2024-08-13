# pacman --upgrade

> Arch Linux 패키지 관리 도구.
> 같이 보기: `pacman`.
> 더 많은 정보: <https://man.archlinux.org/man/pacman.8>.

- 파일에서 하나 이상의 패키지 설치:

`sudo pacman --upgrade {{경로/대상/패키지1.pkg.tar.zst}} {{경로/대상/패키지2.pkg.tar.zst}}`

- 확인 없이 패키지 설치:

`sudo pacman --upgrade --noconfirm {{경로/대상/패키지.pkg.tar.zst}}`

- 패키지 설치 중 충돌하는 파일 덮어쓰기:

`sudo pacman --upgrade --overwrite {{경로/대상/파일}} {{경로/대상/패키지.pkg.tar.zst}}`

- 의존성 버전 검사를 건너뛰고 패키지 설치:

`sudo pacman --upgrade --nodeps {{경로/대상/패키지.pkg.tar.zst}}`

- 영향을 받을 패키지 목록 표시 (패키지를 설치하지 않음):

`pacman --upgrade --print {{경로/대상/패키지.pkg.tar.zst}}`

- 도움말 표시:

`pacman --upgrade --help`
