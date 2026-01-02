# node

> 서버 측 JavaScript 플랫폼 (Node.js).
> 더 많은 정보: <https://nodejs.org/docs/latest/api/cli.html#options>.

- JavaScript 파일 실행:

`node {{경로/대상/파일}}`

- REPL(대화형 셸) 시작:

`node`

- 지정된 파일을 실행하고 가져온 파일이 변경될 때 프로세스를 재시작 (Node.js 버전 18.11+ 필요):

`node --watch {{경로/대상/파일}}`

- 인수로 JavaScript 코드 평가:

`node {{[-e|--eval]}} "{{코드}}"`

- 결과 평가 및 출력, node의 종속성 버전을 출력하는 데 유용:

`node {{[-p|--print]}} "process.versions"`

- 인스펙터 활성화, 소스 코드가 완전히 구문 분석될 때까지 디버거가 연결될 때까지 실행 일시 중지:

`node --no-lazy --inspect-brk {{경로/대상/파일}}`
