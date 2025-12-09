# pmset

> macOS 전원 관리 설정을 구성합니다. 시스템 환경설정 > 에너지 절약에서 할 수 있는 작업과 유사합니다.
> 설정을 수정하는 명령은 `sudo`로 시작해야 합니다.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/pmset.1.html>.

- 현재 전원 관리 설정 표시:

`pmset -g`

- 현재 전원 소스 및 배터리 수준 표시:

`pmset -g batt`

- 디스플레이를 즉시 절전 모드로 전환:

`pmset displaysleepnow`

- 충전기 전원 사용 시 디스플레이가 절전 모드로 전환되지 않도록 설정:

`sudo pmset -c displaysleep 0`

- 배터리 전원 사용 시 디스플레이가 15분 후에 절전 모드로 전환되도록 설정:

`sudo pmset -b displaysleep 15`

- 매주 평일 오전 9시에 컴퓨터가 자동으로 깨어나도록 예약:

`sudo pmset repeat wake MTWRF 09:00:00`

- 시스템 기본값으로 복원:

`sudo pmset -a displaysleep 10 disksleep 10 sleep 30 womp 1`
