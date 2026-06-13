# crystal

> Crystal 소스 코드를 위한 관리도구.
> 더 많은 정보: <https://crystal-lang.org/reference/using_the_compiler>.

- Crystal 파일 실행:

`crystal {{경로/대상/파일.cr}}`

- 단일 실행 파일로의 종속성 및 파일 컴파일:

`crystal build {{경로/대상/파일.cr}}`

- 명령줄 또는 `stdin`에서 Crystal 소스 코드를 읽어 실행:

`crystal eval '{{코드}}'`

- Crystal 파일의 인라인 문서 문자열(docstrings)로부터 API 문서를 생성:

`crystal docs`

- Crystal 테스트 스위트를 컴파일하고 실행:

`crystal spec`

- 언어 테스트를 위한 로컬 대화형 서버 시작:

`crystal play`

- Cystal 응용 프로그램을 위한 프로젝트 디렉토리 생성:

`crystal init app {{애플리케이션_이름}}`

- 도움말 옵션 표시:

`crystal help`
