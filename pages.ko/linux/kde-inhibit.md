# kde-inhibit

> 명령어 실행 중 데스크탑의 다양한 기능을 억제.
> 더 많은 정보: <https://invent.kde.org/plasma/kde-cli-tools/-/blob/master/kdeinhibit/main.cpp>.

- 전원 관리 억제:

`kde-inhibit --power {{명령어}} {{명령어_인자}}`

- 화면 보호기 억제:

`kde-inhibit --screenSaver {{명령어}} {{명령어_인자}}`

- VLC를 실행하고, 실행 중 색 보정(야간 모드)을 억제:

`kde-inhibit --colorCorrect {{vlc}}`
