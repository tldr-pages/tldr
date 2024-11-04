# zypper

> SUSE 및 openSUSE 패키지 관리 도구.
> 다른 패키지 관리자의 동등한 명령을 보려면 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> 더 많은 정보: <https://en.opensuse.org/SDB:Zypper_manual>.

- 사용 가능한 패키지 및 버전 목록 동기화:

`zypper refresh`

- 새 패키지 설치:

`zypper install {{패키지}}`

- 패키지 제거:

`zypper remove {{패키지}}`

- 설치된 패키지를 최신 버전으로 업그레이드:

`zypper update`

- 키워드를 통한 패키지 검색:

`zypper search {{키워드}}`

- 구성된 저장소에 대한 정보 표시:

`zypper repos --sort-by-priority`
