# cupsdisable

> 프린터 및 프린터 클래스를 중단.
> 참고: 목적지는 프린터 또는 프린터 클래스를 나타냄.
> 더 보기: `cupsenable`, `cupsaccept`, `cupsreject`, `lpstat`.
> 더 많은 정보: <https://openprinting.github.io/cups/doc/man-cupsenable.html>.

- 하나 이상의 목적지들을 중지:

`cupsdisable {{목적지1 목적지2 ...}}`

- 지정된 목적지들의 모든 작업 취소:

`cupsdisable -c {{목적지1 목적지2 ...}}`
