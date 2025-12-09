# tre

> 현재 디렉토리의 내용을 트리 형태로 표시.
> 기본적으로 `.gitignore` 설정을 존중합니다.
> 더 많은 정보: <https://github.com/dduan/tre#everything-else>.

- 디렉토리만 출력:

`tre --directories`

- 트리 구조 대신 파일을 포함한 JSON 출력:

`tre --json`

- 지정된 깊이 제한까지 파일 및 디렉토리 출력 (1은 현재 디렉토리를 의미):

`tre --limit {{깊이}}`

- 지정된 색상 모드를 사용하여 모든 숨김 파일 및 디렉토리 출력:

`tre --all --color {{automatic|always|never}}`

- 트리 구조 내 파일들을 출력하고, 각 파일을 연관된 `command`(기본값은 `$EDITOR`)로 열 수 있는 셸 별칭 할당:

`tre --editor {{명령어}}`

- 제공된 정규 표현식과 일치하는 모든 경로를 제외하고 트리 구조 내 파일 출력:

`tre --exclude {{정규_표현식}}`

- 버전 표시:

`tre --version`

- 도움말 표시:

`tre --help`
