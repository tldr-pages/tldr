# vncviewer

> VNC (Virtual Network Computing) 클라이언트를 시작합니다.
> 더 많은 정보: <https://manned.org/vncviewer>.

- 지정된 디스플레이의 호스트에 연결하는 VNC 클라이언트 시작:

`vncviewer {{호스트}}:{{디스플레이_번호}}`

- 전체 화면 모드로 시작:

`vncviewer -FullScreen {{호스트}}:{{디스플레이_번호}}`

- 특정 화면 크기로 VNC 클라이언트 시작:

`vncviewer --geometry {{너비}}x{{높이}} {{호스트}}:{{디스플레이_번호}}`

- 지정된 포트의 호스트에 연결하는 VNC 클라이언트 시작:

`vncviewer {{호스트}}::{{포트}}`
