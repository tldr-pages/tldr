# cupsenable

> 프린터 및 프린터 클래스를 시작.
> 참고: 목적지는 프린터 또는 프린터 클래스를 나타냄.
> 더 보기: `cupsdisable`, `cupsaccept`, `cupsreject`, `lpstat`.
> 더 많은 정보: <https://www.cups.org/doc/man-cupsenable.html>.

- 하나 이상의 목적지들을 시작:

`cupsenable {{목적지1 목적지2 ...}}`

- 목적지의 보류 중인 작업 인쇄를 재개 (`--hold`와 함께 `cupsdisable` 뒤에 사용):

`cupsenable --release {{목적지}}`

- 지정된 목적지들의 모든 작업 취소:

`cupsenable -c {{목적지1 목적지2 ...}}`
