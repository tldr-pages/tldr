# launchctl

> Apple의 `launchd` 관리자에서 시스템 전역 서비스인 시작 데몬과 사용자별 프로그램인 시작 에이전트를 제어.
> `launchd`는 적절한 위치에 배치된 XML 기반 `*.plist` 파일을 로드하고, 정의된 일정에 따라 해당 명령을 실행.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/launchctl.1.html>.

- 사용자가 로그인할 때마다 `launchd`에 로드될 사용자별 에이전트를 활성화:

`launchctl load ~/Library/LaunchAgents/{{내_스크립트}}.plist`

- 루트 권한이 필요하거나 모든 사용자가 로그인할 때마다 로드되어야 하는 에이전트를 활성화 (경로에 `~` 없음에 유의):

`sudo launchctl load /Library/LaunchAgents/{{루트_스크립트}}.plist`

- 시스템이 부팅될 때마다 (사용자가 로그인하지 않아도) 로드될 시스템 전역 데몬을 활성화:

`sudo launchctl load /Library/LaunchDaemons/{{스크립트_대몬}}.plist`

- 모든 로드된 에이전트/데몬을 표시하고, 지정된 프로세스가 현재 실행 중인 경우 PID 및 마지막 실행 시 반환된 종료 코드를 표시:

`launchctl list`

- 현재 로드된 에이전트를 언로드하여 변경 가능 (참고: plist 파일은 재부팅 및/또는 로그인 후에 자동으로 `launchd`에 로드됨):

`launchctl unload ~/Library/LaunchAgents/{{내_스크립트}}.plist`

- 지정된 시간에 관계없이 수동으로 이미 로드된 에이전트/데몬을 실행 (참고: 이 명령은 파일명이 아닌 에이전트의 레이블을 사용):

`launchctl start {{스크립트_파일}}`

- 실행 중인 알려진 에이전트/데몬과 관련된 프로세스를 수동으로 종료:

`launchctl stop {{스크립트_파일}}`
