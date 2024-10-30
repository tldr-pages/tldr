# x0vncserver

> X 디스플레이용 TigerVNC 서버.
> 더 많은 정보: <https://tigervnc.org/doc/x0vncserver.html>.

- 암호 파일을 사용하여 VNC 서버 시작:

`x0vncserver -display {{:0}} -passwordfile {{경로/대상/파일}}`

- 특정 포트를 사용하여 VNC 서버 시작:

`x0vncserver -display {{:0}} -rfbport {{포트}}`
