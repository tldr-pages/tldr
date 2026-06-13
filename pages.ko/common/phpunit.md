# phpunit

> PHPUnit 명령줄 테스트 실행기.
> 더 많은 정보: <https://docs.phpunit.de/en/12.4/textui.html#command-line-options>.

- 현재 디렉토리에서 테스트 실행. 참고: 'phpunit.xml' 파일이 존재해야 합니다:

`phpunit`

- 특정 파일에서 테스트 실행:

`phpunit {{경로/대상/TestFile.php}}`

- 주어진 그룹으로 주석이 달린 테스트 실행:

`phpunit --group {{이름}}`

- 테스트를 실행하고 HTML 형식의 커버리지 보고서 생성:

`phpunit --coverage-html {{경로/대상/폴더}}`
