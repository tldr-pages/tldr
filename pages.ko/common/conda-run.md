# conda run

> conda 환경에서 실행파일(명령어) 실행.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/latest/commands/run.html>.

- 현재 활성화된 환경에서 명령 실행:

`conda run {{명령어}}`

- 이름으로 환경 지정하여 명령 실행:

`conda run {{[-n|--name]}} {{환경_이름}} {{명령어}}`

- 경로(prefix)로 환경 지정하여 명령 실행:

`conda run {{[-p|--prefix]}} {{경로/대상/환경}} {{명령어}}`
