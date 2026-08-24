# kaggle

> Python 3으로 구현된 공식 Kaggle CLI.
> 더 많은 정보: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md>.

- 현재 설정 값 표시:

`kaggle config view`

- 대회 데이터셋에서 특정 파일 다운로드:

`kaggle {{[c|competitions]}} download {{competition}} {{[-f|--file]}} {{경로/대상/파일}}`

- 검색어와 일치하는 대회 목록 표시:

`kaggle {{[c|competitions]}} list {{[-s|--search]}} {{검색어}}`

- 특정 대회에서 사용 가능한 파일 목록 표시:

`kaggle {{[c|competitions]}} files {{대회}}`

- 메시지와 함께 대회에 파일 제출:

`kaggle {{[c|competitions]}} submit {{대회}} {{[-f|--file]}} {{경로/대상/submission.csv}} {{[-m|--message]}} "{{메시지}}"`

- 검색어와 일치하는 데이터셋 목록 표시:

`kaggle {{[d|datasets]}} list {{[-s|--search]}} {{검색어}}`

- 데이터셋의 모든 파일 다운로드:

`kaggle {{[d|datasets]}} download {{소유자}}/{{데이터셋_이름}}`

- 검색어와 일치하는 커널(노트북) 목록 표시:

`kaggle {{[k|kernels]}} list {{[-s|--search]}} {{검색어}}`
