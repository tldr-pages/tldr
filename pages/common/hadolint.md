# hadolint

> Dockerfile linter.
> More information: <https://github.com/hadolint/hadolint>.

- Lint a Dockerfile:

`hadolint {{path/to/Dockerfile}}`

- Lint a Dockerfile outputting a specific format:

`hadolint --format {{json}} {{path/to/Dockerfile}}`

- Lint a Dockerfile ignoring specific rules:

`hadolint --ignore {{DL3006}} --ignore {{DL3008}} {{path/to/Dockerfile}}`

- Lint multiple Dockerfiles while specifying a trusted registry:

`hadolint --trusted-registry {{example.com}}:{{5000}} {{path/to/Dockerfile}} {{path/to/another/Dockerfile}}`
