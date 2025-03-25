# sk

> Rust로 작성된 퍼지 파인더.
> `fzf`와 유사.
> 더 많은 정보: <https://github.com/lotabout/skim>.

- 지정된 디렉터리 내 모든 파일에서 `skim` 시작:

`find {{경로/대상/폴더}} -type f | sk`

- 실행 중인 프로세스에 대해 `skim` 시작:

`ps aux | sk`

- 지정된 쿼리로 `skim` 시작:

`sk --query "{{쿼리}}"`

- `<Shift Tab>`으로 여러 파일 선택 후 파일에 쓰기:

`find {{경로/대상/폴더}} -type f | sk --multi > {{경로/대상/파일}}`
