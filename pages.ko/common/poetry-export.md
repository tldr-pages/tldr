# poetry export

> Poetry의 잠금 파일을 다른 형식으로 내보냄.
> Poetry Export Plugin 제공하는 기능.
> 더 많은 정보: <https://github.com/python-poetry/poetry-plugin-export#usage>.

- 의존성을 `requirements.txt` 파일로 내보내기:

`poetry export {{[-o|--output]}} {{requirements.txt}}`

- 개발 의존성을 포함하여 의존성을 내보내기:

`poetry export {{[-o|--output]}} {{requirements-dev.txt}} --dev`

- 해시를 제외하고 의존성을 내보내기:

`poetry export {{[-o|--output]}} {{requirements.txt}} --without-hashes`

- 지정한 형식으로 의존성을 내보내기:

`poetry export {{[-o|--output]}} {{requirements.txt}} {{[-f|--format]}} {{requirements.txt}}`

- 지정한 의존성 그룹만 내보내기:

`poetry export {{[-o|--output]}} {{requirements.txt}} --only {{main}}`

- 도움말 표시:

`poetry export {{[-h|--help]}}`
