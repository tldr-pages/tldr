# aur sync

> AUR 패키지를 자동으로 다운로드하고 빌드하는 도구.
> 참고: 완전히 사용하려면 `/etc/pacman.conf`에 로컬 저장소가 정의되어 있어야 하며, `vifm`이 설치되어 있어야 합니다.
> 더 많은 정보: <https://github.com/aurutils/aurutils>.

- 하나 이상의 패키지와 의존성을 AUR에서 다운로드하고 빌드한 뒤, 로컬 저장소에 추가:

`aur sync {{패키지1 패키지2 ...}}`

- 로컬 저장소의 패키지 업그레이드:

`aur sync {{[-u|--upgrades]}}`

- 설치 후 빌드 파일 정리:

`aur sync {{[-C|--clean]}} {{패키지}}`

- Vim에서 변경 사항을 확인하지 않고, 의존성 설치도 확인 없이 패키지 설치:

`aur sync --noview {{[-n|--noconfirm]}} {{패키지}}`

- 업그레이드 시 특정 패키지 무시:

`aur sync {{[-u|--upgrades]}} --ignore {{패키지1,패키지2,...}}`
