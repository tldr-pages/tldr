# lstopo

> 시스템의 하드웨어 토폴로지를 보여줍니다.
> 더 많은 정보: <https://manned.org/lstopo>.

- 그래픽 창에서 요약된 시스템 토폴로지 표시 (그래픽 디스플레이가 없는 경우 콘솔에 출력):

`lstopo`

- 요약 없이 전체 시스템 토폴로지 표시:

`lstopo --no-factorize`

- 요약된 시스템 토폴로지를 [p]hysical 인덱스만 사용하여 표시 (즉, OS에서 보는 것처럼):

`lstopo --physical`

- 지정된 형식으로 파일에 전체 시스템 토폴로지 작성:

`lstopo --no-factorize --output-format {{콘솔|ascii|tex|fig|svg|pdf|ps|png|xml}} {{경로/대상/파일}}`

- 단색 또는 회색조로 출력:

`lstopo --palette {{없음|회색}}`
