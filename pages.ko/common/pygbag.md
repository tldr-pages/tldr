# pygbag

> Pygame 프로젝트를 WebAssembly으로 패키징하여 웹 브라우저에서 실행할 수 있도록 함.
> 더 많은 정보: <https://github.com/pygame-web/pygbag#pygbag>.

- Pygame 프로젝트를 패키징하고 로컬 테스트 서버 시작:

`pygbag {{경로/대상/프로젝트_폴더}}`

- Python 모듈 방식으로 프로젝트 패키징:

`python -m pygbag {{경로/대상/프로젝트_폴더}}`

- 테스트 서버를 시작하지 않고 프로젝트 패키징 및 빌드:

`pygbag {{경로/대상/프로젝트_폴더}} --build`

- 지정한 템플릿을 사용하여 프로젝트 패키징:

`pygbag {{경로/대상/프로젝트_폴더}} --template {{템플릿_이름.tmpl}}`

- <https://itch.io>용 ZIP 아카이브 생성:

`pygbag {{경로/대상/프로젝트_폴더}} --archive`

- 최적화를 비활성화하여 프로젝트 패키징:

`pygbag {{경로/대상/프로젝트_폴더}} --no_opt`

- 테스트 서버의 포트 지정:

`pygbag {{경로/대상/프로젝트_폴더}} --port {{8080}}`

- 도움말 표시:

`pygbag {{[-h|--help]}}`
