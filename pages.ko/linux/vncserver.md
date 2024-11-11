# vncserver

> VNC (Virtual Network Computing) 데스크톱 시작.
> 더 많은 정보: <https://manned.org/vncserver.1x>.

- 다음 사용 가능한 디스플레이에 VNC 서버 시작:

`vncserver`

- 특정 화면 크기로 VNC 서버 시작:

`vncserver --geometry {{너비}}x{{높이}}`

- 특정 디스플레이에서 실행 중인 VNC 서버 인스턴스 종료:

`vncserver --kill :{{디스플레이_번호}}`
