# hadolint

> Dockerfile 린터.
> 더 많은 정보: <https://github.com/hadolint/hadolint>.

- Dockerfile 린트:

`hadolint {{경로/대상/Dockerfile}}`

- Dockerfile을 린트하여, 출력을 JSON 형식으로 표시:

`hadolint --format {{json}} {{경로/대상/Dockerfile}}`

- Dockerfile을 린트하여, 특정 형식으로 출력을 표시:

`hadolint --format {{tty|json|checkstyle|codeclimate|codacy}} {{경로/대상/Dockerfile}}`

- 특정 규칙을 무시하고 Dockerfile을 린트:

`hadolint --ignore {{DL3006}} --ignore {{DL3008}} {{경로/대상/Dockerfile}}`

- 특정 신뢰할 수 있는 레지스트리를 사용하여 여러 Dockerfile을 린트하는 것:

`hadolint --trusted-registry {{docker.io}} --trusted-registry {{example.com}}:{{5000}} {{경로/대상/Dockerfile1 경로/대상/Dockerfile2 ...}}`
