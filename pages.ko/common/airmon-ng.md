# airmon-ng

> 무선 네트워크 장치에서 모니터 모드를 활성화.
> `aircrack-ng`의 일부.
> 더 많은 정보: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- 무선 장치 및 상태를 나열:

`sudo airmon-ng`

- 특정 장치에 대한 모니터 모드 실행:

`sudo airmon-ng start {{wlan0}}`

- 무선 장치를 사용하는 방해되는 프로세스를 종료:

`sudo airmon-ng check kill`

- 특정 네트워크 인터페이스에 대한 모니터 모드 종료:

`sudo airmon-ng stop {{wlan0mon}}`
