# cupsreject

> 프린터로 전송된 작업 거부.
> 참고: 목적지는 프린터 또는 프린터 클래스를 나타냄.
> 더 보기: `cupsaccept`, `cupsenable`, `cupsdisable`, `lpstat`.
> 더 많은 정보: <https://www.cups.org/doc/man-cupsaccept.html>.

- 지정된 목적지로의 인쇄 작업 거부:

`cupsreject {{목적지1 목적지2 ...}}`

- 다른 서버 지정:

`cupsreject -h {{서버}} {{목적지1 목적지2 ...}}`

- 이유 문자열을 지정 (기본적으로 "Reason Unknown"):

`cupsreject -r {{이유}} {{목적지1 목적지2 ...}}`
