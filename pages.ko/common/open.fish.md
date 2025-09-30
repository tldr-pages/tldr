# open

> 파일, 디렉토리 및 URI를 기본 애플리케이션으로 엽니다.
> 이 명령은 내장 `open` 명령이 없는 운영 체제(예: Haiku 및 macOS)에서 fish를 통해 사용할 수 있습니다.
> 더 많은 정보: <https://fishshell.com/docs/current/cmds/open.html>.

- 관련 애플리케이션으로 파일 열기:

`open {{경로/대상/파일.ext}}`

- 현재 디렉토리에서 주어진 확장자를 가진 모든 파일을 관련 애플리케이션으로 열기:

`open {{*.ext}}`

- 기본 파일 관리자로 디렉토리 열기:

`open {{경로/대상/폴더}}`

- 기본 웹 브라우저로 웹사이트 열기:

`open {{https://example.com}}`

- 처리할 수 있는 기본 애플리케이션으로 특정 URI 열기:

`open {{tel:123}}`
