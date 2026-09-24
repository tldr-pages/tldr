# pip config

> pip 로컬 및 전역 설정 관리.
> 더 많은 정보: <https://pip.pypa.io/en/stable/cli/pip_config/>.

- 모든 설정 값 목록 표시:

`pip config list`

- 설정 파일과 해당 값 표시:

`pip config debug`

- 명령 옵션 값 설징:

`pip config set {{명령어.옵션}} {{값}} {{--global|--user|--site}}`

- 명령 옵션 값 조회:

`pip config get {{명령어.옵션}} {{--global|--user|--site}}`

- 명령 옵션 값 제거:

`pip config unset {{명령어.옵션}} {{--global|--user|--site}}`

- 기본 편집기로 설정 파일 편집:

`pip config edit {{--global|--user|--site}}`

- 특정 편집기로 설정 파일 편집:

`pip config edit {{--global|--user|--site}} --editor {{경로/대상/편집기_실행파일}}`
