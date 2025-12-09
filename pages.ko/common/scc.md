# scc

> 코드 라인 수를 계산합니다. Go로 작성되었습니다.
> 더 많은 정보: <https://github.com/boyter/scc>.

- 현재 디렉토리의 코드 라인 수 출력:

`scc`

- 대상 디렉토리의 코드 라인 수 출력:

`scc {{경로/대상/폴더}}`

- 각 파일에 대한 출력 표시:

`scc --by-file`

- 특정 출력 형식을 사용하여 출력 표시 (기본값은 `tabular`):

`scc --format {{tabular|wide|json|csv|cloc-yaml|html|html-table}}`

- 특정 파일 확장자를 가진 파일만 계산:

`scc --include-ext {{go,java,js}}`

- 카운트에서 제외할 디렉토리 지정:

`scc --exclude-dir {{.git,.hg}}`

- 출력 및 정렬 기준 열로 정렬 (기본값은 파일 기준):

`scc --sort {{files|name|lines|blanks|code|comments|complexity}}`

- 도움말 표시:

`scc -h`
