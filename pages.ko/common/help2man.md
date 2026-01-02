# help2man

> 실행 파일의 `--help` 및 `--version` 출력에서 간단한 매뉴얼 페이지 생성.
> 더 많은 정보: <https://www.gnu.org/software/help2man/#Invoking-help2man>.

- 실행 파일에 대한 매뉴얼 페이지를 생성:

`help2man {{실행파일}}`

- man 페이지에서 "이름" 단락을 지정:

`help2man {{실행파일}} --name {{이름}}`

- man 페이지의 섹션을 지정 (기본값은 1):

`help2man {{실행파일}} --section {{섹션}}`

- `stdout` 대신 파일로 출력:

`help2man {{실행파일}} --output {{경로/대상/파일}}`

- 도움말 표시:

`help2man --help`
