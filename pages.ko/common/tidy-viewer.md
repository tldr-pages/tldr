# tidy-viewer

> CSV, TSV, PSV, Parquet 및 Arrow IPC 파일을 열 스타일과 함께 보기 좋게 출력.
> 일반적으로 `tv`라는 별칭으로도 사용됨.
> 더 많은 정보: <https://github.com/alexhallam/tv#help>.

- CSV 파일의 첫 25개 행을 보기 좋게 추력:

`tidy-viewer {{경로/대상/파일.csv}}`

- `stdin`으로 전달된 데이터를 보기 좋게 출력:

`cat {{경로/대상/파일.csv}} | tidy-viewer`

- 사용자 지정 구분자([s]eparator)를 사용해 파일 출력 (예: 파이프):

`tidy-viewer {{[-s|--delimiter]}} '|' {{경로/대상/파일.psv}}`

- 지정한 색상 팔레트로 데이터 표시 (1: nord, 2: one_dark, 3: gruvbox, 4: dracula, 5: solarized light):

`tidy-viewer {{[-c|--color]}} {{3}} {{경로/대상/파일.csv}}`

- 모든 행을 컬러로 출력하고, 페이지 단위로 타색:

`tidy-viewer {{[-af|--color-always --force-all-rows]}} {{경로/대상/파일.csv}} | less -RS`

- 도움말 표시:

`tidy-viewer {{[-h|--help]}}`

- 버전 정보 표시:

`tidy-viewer {{[-V|--version]}}`
