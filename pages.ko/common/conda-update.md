# conda update

> conda 환경 내 패키지(conda 자체도 포함) 업데이트.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/latest/commands/update.html>.

- 현재 환경의 모든 패키지 업데이트:

`conda update {{[--all|--update-all]}}`

- 현재 환경의 특정 패키지 업데이트:

`conda update {{패키지_이름}}`

- base 환경에서 conda 자체 업데이트:

`conda update {{[-n|--name]}} base conda`

- 고정된 패키지를 무시하고 패키지 업데이트:

`conda update --no-pin`

- 오프라인 모드에서 패키지 업데이트:

`conda update --offline`
