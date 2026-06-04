# kaggle competitions

> Kaggle 대회 관리.
> 더 많은 정보: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#competitions>.

- 모든 대회 목록 표시:

`kaggle {{[c|competitions]}} list`

- 대회 데이터 다운로드:

`kaggle {{[c|competitions]}} download {{대회_이름}}`

- 특정 파일 다운로드:

`kaggle {{[c|competitions]}} download {{대회_이름}} {{[-f|--file]}} {{file}}`

- 대회에 파일 제출:

`kaggle {{[c|competitions]}} submit {{대회_이름}} {{[-f|--file]}} {{path/to/file}} {{[-m|--message]}} "{{메시지}}"`

- 리더보드 표시 또는 다운로드:

`kaggle {{[c|competitions]}} leaderboard {{대회_이름}} {{--show|--download}}`

- 제출 목록 조회:

`kaggle {{[c|competitions]}} submissions {{대회_이름}}`
