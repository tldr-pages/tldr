# pydocstyle

> Python 스크립트가 Python 도크스트링 규칙을 준수하는지 정적 검사합니다.
> 더 많은 정보: <https://www.pydocstyle.org/en/latest/>.

- Python 스크립트 또는 특정 디렉터리의 모든 Python 스크립트 분석:

`pydocstyle {{파일.py|경로/대상/폴더}}`

- 각 오류에 대한 설명 표시:

`pydocstyle {{[-e|--explain]}} {{파일.py|경로/대상/폴더}}`

- 디버그 정보 표시:

`pydocstyle {{[-d|--debug]}} {{파일.py|경로/대상/폴더}}`

- 총 오류 수 표시:

`pydocstyle --count {{파일.py|경로/대상/폴더}}`

- 특정 구성 파일 사용:

`pydocstyle --config {{경로/대상/구성_파일}} {{파일.py|경로/대상/폴더}}`

- 하나 이상의 오류 무시:

`pydocstyle --ignore {{D101,D2,D107,...}} {{파일.py|경로/대상/폴더}}`

- 특정 규약의 오류 검사:

`pydocstyle --convention {{pep257|numpy|google}} {{파일.py|경로/대상/폴더}}`
