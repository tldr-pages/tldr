# mocha

> 기능이 풍부한 JavaScript 테스트 프레임워크.
> 더 많은 정보: <https://mochajs.org>.

- 기본 설정 또는 `mocha.opts`에 구성된 대로 테스트 실행:

`mocha`

- 특정 위치에 포함된 테스트 실행:

`mocha {{테스트가_있는_디렉토리}}`

- 특정 `grep` 패턴과 일치하는 테스트 실행:

`mocha --grep {{정규_표현식}}`

- 현재 디렉토리의 JavaScript 파일 변경 시 및 최초 실행 시 테스트 실행:

`mocha --watch`

- 특정 리포터로 테스트 실행:

`mocha --reporter {{리포터}}`
