# tuptime

> 시스템 재시작 이후에도 기록을 유지하면서, 시스템의 누적 실행 시간과 관련 통계를 표시.
> `uptime`과 유사하지만, 부팅 횟수, 정상/비정상 종료 횟수, 업타임/다운타임 비율, 최초 부팅 이후의 평균값 등을 추가로 제공.
> 더 많은 정보: <https://github.com/rfmoz/tuptime>.

- 시스템 업타임 이력과 통계 표시:

`tuptime`

- 시스템 수명 정보를 표 형식으로 표시:

`tuptime --table`

- 시스템 수명 정보를 목록 형식으로 표시:

`tuptime --list`

- 커널 버전과 부팅 ID를 포함하여 표 형식으로 표시:

`tuptime --table --kernel --bootid`

- 지정한 부팅 범위의 정보 표시:

`tuptime --table --since {{1}} --until {{5}}`

- 지정한 초 이전부터의 기록만 표시 (예: 1년 = 31557600):

`tuptime --tsince -{{31557600}}`

- 시간을 초 단위로 날짜/시간을 epoch 형식으로 출력:

`tuptime --seconds`

- CSV 형식으로 출력:

`tuptime --csv`
