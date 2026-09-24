# kaggle kernels

> Kaggle 커널 관리.
> 더 많은 정보: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#kernels>.

- 모든 커널 목록 표시:

`kaggle {{[k|kernels]}} list`

- 커널 출력 파일 목록 표시:

`kaggle {{[k|kernels]}} files {{커널_이름}}`

- 커널용 메타데이터 파일 초기화 (기본값: 현재 디렉터리):

`kaggle {{[k|kernels]}} init {{[-p|--path]}} {{경로/대상/디렉터리}}`

- 새 코드를 커널에 업로드하고 실행:

`kaggle {{[k|kernels]}} push {{[-p|--path]}} {{경로/대상/디렉터리}}`

- 커널 가져오기:

`kaggle {{[k|kernels]}} pull {{커널_이름}} {{[-p|--path]}} {{경로/대상/디렉터리}}`

- 최신 커널 실행 결과 데이터 가져오기:

`kaggle {{[k|kernels]}} output {{커널_이름}}`

- 최신 커널 실행 상태 표시:

`kaggle {{[k|kernels]}} status {{커널_이름}}`
