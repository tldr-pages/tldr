# slim

> Docker 이미지를 분석하고 최적화.
> 더 많은 정보: <https://github.com/slimtoolkit/slim#usage-details>.

- 대화형 모드로 Slim을 시작:

`slim`

- 특정 Docker 이미지의 레이어를 분석:

`slim xray --target {{이미지:태그}}`

- Dockerfile을 검사:

`slim lint --target {{경로/대상/Dockerfile}}`

- Docker 이미지를 분석하고 최적화된 이미지를 생성:

`slim build {{이미지:태그}}`

- 하위 명령어의 도움말을 표시:

`slim {{하위명령어}} --help`
