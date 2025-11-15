# iw

> 무선 장치를 표시하고 조작.
> 같이 보기: `iw dev`.
> 더 많은 정보: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- 사용 가능한 무선 네트워크 스캔:

`iw dev {{wlp}} scan`

- 오픈된 무선 네트워크에 연결:

`iw dev {{wlp}} connect {{SSID}}`

- 현재 연결 종료:

`iw dev {{wlp}} disconnect`

- 현재 연결 정보 표시:

`iw dev {{wlp}} link`

- 모든 물리적 및 논리적 무선 네트워크 인터페이스 나열:

`iw dev`

- 모든 물리적 하드웨어 인터페이스의 무선 기능 나열:

`iw phy`

- 커널의 현재 무선 규제 도메인 정보 나열:

`iw reg get`

- 모든 명령에 대한 도움말 표시:

`iw help`
