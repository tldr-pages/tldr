# cupsaccept

> 목적지로 전송된 작업을 수락.
> 참고: 목적지는 프린터 또는 프린터 클래스라고 함.
> 추가 정보: `cupsreject`, `cupsenable`, `cupsdisable`, `lpstat`.
> 더 많은 정보: <https://www.cups.org/doc/man-cupsaccept.html>.

- 지정된 목적지로 인쇄 작업 수락:

`cupsaccept {{목적지1 목적지2 ...}}`

- 다른 서버 지정:

`cupsaccept -h {{서버}} {{목적지1 목적지2 ...}}`
