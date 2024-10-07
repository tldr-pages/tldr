# git filter-repo

> Git 히스토리를 재작성하는 다목적 도구.
> 같이 보기: `bfg`.
> 더 많은 정보: <https://github.com/newren/git-filter-repo>.

- 모든 파일에서 민감한 문자열 대체:

`git filter-repo --replace-text <(echo '{{찾을_문자열}}==>{{대체할_문자열}}')`

- 특정 폴더를 히스토리를 유지하면서 추출:

`git filter-repo --path {{경로/대상/폴더}}`

- 특정 폴더를 히스토리를 유지하면서 제거:

`git filter-repo --path {{경로/대상/폴더}} --invert-paths`

- 하위 폴더의 모든 파일을 한 단계 위로 이동:

`git filter-repo --path-rename {{경로/대상/폴더/:}}`
