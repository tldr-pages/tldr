# nodemon

> 파일을 감시하고 변경 사항이 감지되면 Node 애플리케이션을 자동으로 재시작.
> 더 많은 정보: <https://github.com/remy/nodemon/tree/main/doc/cli>.

- 지정된 파일을 실행하고 특정 파일의 변경 사항 감시:

`nodemon {{경로/대상/파일.js}}`

- 수동으로 nodemon 재시작(이 기능을 사용하려면 nodemon이 이미 활성 상태여야 함):

`rs`

- 특정 파일 무시:

`nodemon --ignore {{경로/대상/파일_또는_폴더}}`

- Node 애플리케이션에 인수 전달:

`nodemon {{경로/대상/파일.js}} {{인수들}}`

- nodemon 인수가 아닌 경우 Node 자체에 인수 전달(예: `--inspect`):

`nodemon {{인수들}} {{경로/대상/파일.js}}`

- 임의의 비-Node 스크립트 실행:

`nodemon --exec "{{스크립트를_실행할_명령}} {{옵션들}}" {{경로/대상/스크립트}}`

- Python 스크립트 실행:

`nodemon --exec "python {{옵션들}}" {{경로/대상/파일.py}}`
