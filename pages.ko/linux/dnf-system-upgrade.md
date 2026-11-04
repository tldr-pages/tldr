# dnf system-upgrade

> Fedora를 새로운 메이저 버전으로 업그레이드.
> 더 많은 정보: <https://dnf5.readthedocs.io/en/latest/commands/system-upgrade.8.html>.

- 설치된 모든 패키지를 업데이트하여 시스템 준비:

`sudo dnf upgrade --refresh`

- 새로운 릴리스 버전에 필요한 패키지 다운로드:

`sudo dnf system-upgrade download --releasever {{릴리스_버전}}`

- 시스템을 재부팅하고 업그레이드 시작:

`sudo dnf system-upgrade reboot`

- 현재 업그레이드 작업 상태 표시:

`sudo dnf system-upgrade status`

- 이전 업그레이드 시도의 로그 표시:

`sudo dnf system-upgrade log`

- 캐시된 업그레이드 데이터 및 패키지 삭제:

`sudo dnf system-upgrade clean`
