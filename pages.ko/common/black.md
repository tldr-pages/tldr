# black

> Python 자동 코드 formatter.
> 더 많은 정보: <https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html>.

- 파일 또는 전체 디렉토리의 자동 포맷:

`black {{파일_또는_디렉토리/의/경로}}`

- 전달된 코드를 문자열로 포맷:

`black -c {{파일_또는_디렉토리/의/경로}}`

- 표준 출력시 각 파일에 대해 diff 출력:

`black --diff {{파일_또는_디렉토리/의/경로}}`

- 파일을 다시 쓰지 않고 상태 반환:

`black --check {{파일_또는_디렉토리/의/경로}}`

- 파일 또는 디렉토리가 stderr에 배타적 오류 메시지를 발생시키는 자동 포맷:

`black --quiet {{파일_또는_디렉토리/의/경로}}`

- 작은 따옴표를 큰 따옴표로 바꾸지 않고 파일 또는 디렉토리 자동 서식 지정(채택 도우미, 새 프로젝트에 사용하지 마세요):

`black --skip-string-normalization {{파일_또는_디렉토리/의/경로}}`
