# conda activate

> conda 환경 활성화.
> 관련 항목: `conda deactivate`.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/stable/dev-guide/deep-dives/activation.html>.

- 이름이 `myenv`인 기존 환경 활성화:

`conda activate myenv`

- 사용자 지정 경로에 위치한 기존 환경 활성화:

`conda activate {{경로/대상/myenv}}`

- 이전 환경 위에 `myenv` 환경으로 덮어 두 환경의 라이브러리/명령어/변수 모두 접근 가능하게 설정:

`conda activate --stack myenv`

- 이전 환경을 덮어쓰지 않고 myenv 환경을 깨끗하게 시작하여, 이전 환경의 라이브러리/명령어/변수에 접근하지 않도록 설정:

`conda activate --no-stack myenv`

- 도움말 표시:

`conda activate {{[-h|--help]}}`
