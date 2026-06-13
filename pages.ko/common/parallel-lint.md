# parallel-lint

> PHP 파일의 구문을 병렬로 검사.
> 더 많은 정보: <https://github.com/JakubOnderka/PHP-Parallel-Lint>.

- 특정 디렉토리의 구문 검사:

`parallel-lint {{경로/대상/폴더}}`

- 지정된 병렬 프로세스 수를 사용하여 디렉토리 구문 검사:

`parallel-lint -j {{프로세스_수}} {{경로/대상/폴더}}`

- 특정 디렉토리를 제외하고 디렉토리 구문 검사:

`parallel-lint --exclude {{경로/대상/제외_폴더}} {{경로/대상/폴더}}`

- 쉼표로 구분된 확장자 목록을 사용하여 파일 디렉토리의 구문 검사:

`parallel-lint -e {{php,html,phpt}} {{경로/대상/폴더}}`

- 디렉토리의 구문 검사를 수행하고 결과를 JSON으로 출력:

`parallel-lint --json {{경로/대상/폴더}}`

- 디렉토리의 구문 검사를 수행하고 오류가 있는 행에 대한 Git Blame 결과 표시:

`parallel-lint --blame {{경로/대상/폴더}}`
