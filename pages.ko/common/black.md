# black

> Python 자동 코드 formatter. 
> 자세한 정보: <https://github.com/psf/black>.

- 파일 또는 전체 디렉토리의 자동 포맷:

`black {{path/to/file_or_directory}}`

- 전달된 코드를 문자열로 포맷:

`black -c {{path/to/file_or_directory}}`

- 표준 출력시 각 파일에 대해 diff 출력:

`black --diff {{path/to/file_or_directory}}`

- 파일을 다시 쓰지 않고 상태 반환:

`black --check {{path/to/file_or_directory}}`

- 파일 또는 디렉토리가 stderr에 배타적 오류 메시지를 발생시키는 자동 포맷:

`black --quiet {{path/to/file_or_directory}}`