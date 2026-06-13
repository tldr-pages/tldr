# volta

> Node.js 런타임, npm 및 Yarn 패키지 관리자 또는 npm에서 제공하는 바이너리를 설치하는 JavaScript 도구 관리자.
> 더 많은 정보: <https://docs.volta.sh/reference/>.

- 설치된 모든 도구 나열:

`volta list`

- 최신 버전의 도구 설치:

`volta install {{node|npm|yarn|패키지_이름}}`

- 특정 버전의 도구 설치:

`volta install {{node|npm|yarn}}@version`

- 프로젝트에 사용할 도구 버전 선택 (`package.json`에 저장됨):

`volta pin {{node|npm|yarn}}@version`

- 도움말 표시:

`volta help`

- 하위 명령에 대한 도움말 표시:

`volta help {{fetch|install|uninstall|pin|list|completions|which|setup|run|help}}`
