# git check-ignore

> Git ignore/exclude (".gitignore") 파일을 분석하고 디버깅.
> 더 많은 정보: <https://git-scm.com/docs/git-check-ignore>.

- 파일 또는 폴더가 무시되는지 확인:

`git check-ignore {{경로/대상/파일_또는_폴더}}`

- 여러 파일 또는 폴더가 무시되는지 확인:

`git check-ignore {{경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...}}`

- 각 경로를 한 줄씩 `stdin`에서 사용:

`git check-ignore --stdin < {{경로/대상/파일_목록}}`

- 색인을 확인하지 않음 (경로가 추적되고 무시되지 않은 이유를 디버그하는 데 사용):

`git check-ignore --no-index {{경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...}}`

- 각 경로에 대한 일치하는 패턴에 대한 세부 정보 포함:

`git check-ignore {{[-v|--verbose]}} {{경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...}}`
