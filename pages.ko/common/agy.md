# agy

> Google의 에이전트 기반 개발 플랫폼.
> 더 많은 정보: <https://antigravity.google/docs>.

- 특정 파일 또는 디렉터리 열기:

`agy {{경로/대상/파일_또는_디렉터리}}`

- 두 파일을 비교:

`agy {{[-d|--diff]}} {{경로/대상/파일1}} {{경로/대상/파일2}}`

- 현재 작업 디렉터리에서 프롬프트를 사용해 채팅 세션 실행:

`agy chat "{{프롬프트}}"`

- 특정 확장 설치 또는 제거:

`agy --{{install|uninstall}}-extension {{publisher.extension|경로/대상/extension.vsix}}`

- 사용자 프로필에 MCP (Model Context Protocol) 서버 정의 추가:

`agy --add-mcp "{{json_문자열}}"`

- 도움말 표시:

`agy {{[-h|--help]}}`
