# conda rename

> 기존 conda 환경 이름 변경.
> The base 환경과 현재 활성화된 환경은 이름 변경 불가.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/latest/commands/rename.html>.

- 이름을 사용하여 환경 이름 변경:

`conda rename {{[-n|--name]}} {{현재_이름}} {{새로운_이름}}`

- 전체 경로(prefix)를 사용하여 환경 이름 변경:

`conda rename {{[-p|--prefix]}} {{경로/대상/환경}} {{새로운_이름}}`
