# vnstati

> vnStat의 PNG 이미지 출력 지원.
> 더 많은 정보: <https://manned.org/vnstati>.

- 지난 2개월, 일별 및 전체 요약 출력:

`vnstati --summary --iface {{네트워크_인터페이스}} --output {{경로/대상/출력.png}}`

- 역대 트래픽이 가장 많은 10일 출력:

`vnstati --top 10 --iface {{네트워크_인터페이스}} --output {{경로/대상/출력.png}}`

- 지난 12개월의 월별 트래픽 통계 출력:

`vnstati --months --iface {{네트워크_인터페이스}} --output {{경로/대상/출력.png}}`

- 지난 24시간의 시간별 트래픽 통계 출력:

`vnstati --hours --iface {{네트워크_인터페이스}} --output {{경로/대상/출력.png}}`
