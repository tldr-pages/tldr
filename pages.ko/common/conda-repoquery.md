# conda repoquery

> conda 저장소에서 고급 패키지 검색 수행.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/latest/commands/repoquery/index.html>.

- 지정한 패키지의 사용 가능한 버전 표시:

`conda repoquery search {{패키지}}`

- 지정한 패키지의 의존성 표시:

`conda repoquery depends {{패키지}}`

- 지정한 패키지에 의존하는 패키지 표시:

`conda repoquery whoneeds {{패키지}}`
