# clip-view

> 명령줄 인터페이스 페이지 렌더링.
> 훨씬 더 광범위한 구문과 여러 렌더링 모드를 사용해 TlDr과 유사한 프로젝트를 렌더링.
> 더 많은 정보: <https://github.com/command-line-interface-pages/v2-tooling/tree/main/clip-view>.

- 특정 로컬 페이지 렌더링:

`clip-view {{경로/대상/페이지1.clip 경로/대상/페이지2.clip ...}}`

- 특정 원격 페이지 렌더링:

`clip-view {{페이지_이름1 페이지_이름2 ...}}`

- 특정 렌더링으로 페이지 렌더링:

`clip-view --render {{tldr|tldr-colorful|docopt|docopt-colorful}} {{페이지_이름1 페이지_이름2 ...}}`

- 특정 색상 테마로 페이지 렌더링:

`clip-view --theme {{경로/대상/로컬_테마.yaml|원격_테마_이름}} {{페이지_이름1 페이지_이름2...}}`

- 페이지 또는 테마 캐시 지우기:

`clip-view --clear-{{페이지|테마}}-cache`

- 도움말 표시:

`clip-view --help`

- 버전정보 표시:

`clip-view --version`
