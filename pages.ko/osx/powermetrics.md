# powermetrics

> CPU 사용량, 전력 및 인터럽트 wakeup 통계를 수집하고 표시.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/powermetrics.1.html>.

- 기본 5초 샘플링 간격으로 CPU, 전력 및 wakeup 지표 표시:

`sudo powermetrics`

- 2000 밀리초마다 지표를 샘플링하고 10개의 샘플을 수집한 후 종료:

`sudo powermetrics {{[-i|--sample-rate]}} 2000 {{[-n|--sample-count]}} 10`

- `stdout` 대신 파일에 출력을 저장:

`sudo powermetrics {{[-o|--output-file]}} {{경로/대상/출력파일.txt}}`

- 지정한 방식으로 프로세스 목록 정렬(기본값: `composite`):

`sudo powermetrics {{[-r|--order]}} {{pid|wakeups|cputime|composite}}`

- 머신이 처리하기 쉬운 property list 형식으로 출력하고 종료 시 사용량 요약 표시:

`sudo powermetrics {{[-f|--format]}} plist --show-usage-summary`
