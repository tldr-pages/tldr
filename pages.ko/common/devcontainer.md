# devcontainer

> Docker 컨테이너를 개발 환경으로 사용.
> 더 많은 정보: <https://containers.dev/implementors/reference/>.

- Dev Container 생성 및 실행:

`devcontainer up`

- 작업 공간에 Dev Container 템플릿을 적용:

`devcontainer templates apply --template-id {{템플릿_아이디}} --template-args {{템플릿_매개변수}} --workspace-folder {{경로/대상/작업공간}}`

- 현재 작업공간에서 실행 중인 Dev Container에 명령을 실행:

`devcontainer exec {{명령어}}`

- `devcontainer.json`에서 Dev Container 이미지를 빌드:

`devcontainer build {{경로/대상/작업공간}}`

- VS Code에서 Dev 컨테이너를 열기 (경로는 선택사항):

`devcontainer open {{경로/대상/작업공간}}`

- `devcontainer.json`에서 Dev Container의 구성을 읽고 출력:

`devcontainer read-configuration`
