# conda list

> conda 환경에 설치된 패키지 목록 표시.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/stable/commands/list.html>.

- 현재 환경의 모든 패키지 목록 표시:

`conda list`

- 지정한 이름의 환경에 설치된 패키지 목록 표시:

`conda list {{[-n|--name]}} {{환경}}`

- 지정한 경로(prefix)에 설치된 패키지 목록 표시:

`conda list {{[-p|--prefix]}} {{경로/대상/환경}}`

- `regex`를 사용하여 설치된 패키지 필터링:

`conda list {{정규식}}`

- 나중에 사용할 수 있도록 패키지 목록 저장:

`conda list {{[-e|--export]}} > {{경로/대상/패키지-목록.txt}}`
