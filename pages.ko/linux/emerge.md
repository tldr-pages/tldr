# emerge

> Gentoo Linux 패키지 관리 도구.
> 다른 패키지 관리자의 동등한 명령을 보려면 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> 더 많은 정보: <https://wiki.gentoo.org/wiki/Portage#emerge>.

- 모든 패키지 동기화:

`emerge --sync`

- 모든 패키지 및 의존성 업데이트:

`emerge {{[-avuDN|--ask --verbose --update --deep --newuse]}} @world`

- 업데이트 실패 시, 실패한 패키지를 건너뛰고 다시 시작:

`emerge --resume --skipfirst`

- 새 패키지 설치 시, 확인 요청:

`emerge {{[-av|--ask --verbose]}} {{패키지}}`

- 패키지 제거 시, 확인 요청:

`emerge -Cav {{패키지}}`

- 고아 패키지 제거 (의존성으로만 설치된 패키지):

`emerge {{[-avc|--ask --verbose --depclean]}}`

- 패키지 데이터베이스에서 키워드 검색:

`emerge {{[-S|--searchdesc]}} {{키워드}}`
