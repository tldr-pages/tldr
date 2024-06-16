# pacman

> Arch Linux 패키지 관리 도구.
> 같이 보기: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
> 다른 패키지 관리자의 동등한 명령을 보려면 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> 더 많은 정보: <https://man.archlinux.org/man/pacman.8>.

- 모든 패키지를 동기화하고 업데이트:

`sudo pacman -Syu`

- 새 패키지 설치:

`sudo pacman -S {{패키지}}`

- 특정 패키지 및 의존성 제거:

`sudo pacman -Rs {{패키지}}`

- 특정 파일이 포함된 패키지를 데이터베이스에서 검색:

`pacman -F "{{파일_이름}}"`

- 설치된 패키지 및 버전 나열:

`pacman -Q`

- 명시적으로 설치된 패키지 및 버전만 나열:

`pacman -Qe`

- 고아 패키지(의존성으로 설치되었지만 더 이상 어떤 패키지도 필요로 하지 않는 패키지) 나열:

`pacman -Qtdq`

- 전체 `pacman` 캐시 삭제:

`sudo pacman -Scc`
