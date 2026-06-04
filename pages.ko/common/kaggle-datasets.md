# kaggle datasets

> Kaggle 데이터셋 관맄.
> 더 많은 정보: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#datasets>.

- 특정 사용자 또는 조직이 소유한 모든 데이터셋 목록 표시:

`kaggle {{[d|datasets]}} list --user {{사용자명}}`

- 이름으로 데이터셋 검색:

`kaggle {{[d|datasets]}} list {{[-s|--search]}} "{{데이터셋_이름}}"`

- 데이터셋 다운로드:

`kaggle {{[d|datasets]}} download "{{데이터셋_이름}}"`

- 공개 데이터셋 생성:

`kaggle {{[d|datasets]}} create {{[-p|--path]}} {{경로/대상/데이터셋}} {{[-u|--public]}}`

- 데이터셋 메타데이터 다운로드:

`kaggle {{[d|datasets]}} metadata {{데이터셋_이름}}`

- 데이터셋용 메타데이터 초기화:

`kaggle {{[d|datasets]}} init {{[-p|--path]}} {{경로/대상/데이터셋}}`

- 데이터셋 삭제:

`kaggle {{[d|datasets]}} delete {{데이터셋_이름}}`
