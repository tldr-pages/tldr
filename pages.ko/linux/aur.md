# aur

> AUR에서 패키지를 빌드하고 로컬 저장소를 관리합니다.
> 참고: 이 기능을 완전히 사용하려면 `/etc/pacman.conf`에 로컬 저장소가 정의되어 있어야 하며 `vifm`이 설치되어 있어야 합니다.
> 더 많은 정보: <https://github.com/aurutils/aurutils>.

- AUR 데이터베이스에서 패키지 검색:

`aur search {{키워드}}`

- AUR에서 패키지와 그 의존성을 다운로드하고 빌드하여 로컬 저장소에 추가:

`aur sync {{패키지}}`

- 로컬 저장소에 있는 패키지 [l]목록:

`aur repo {{[-l|--list]}}`

- 로컬 저장소 패키지 업그레이드:

`aur sync {{[-u|--upgrades]}}`

- Vim에서 변경 사항을 보지 않고 패키지를 설치하며, 의존성 설치를 확인하지 않음:

`aur sync --noview {{[-n|--noconfirm]}} {{패키지}}`
