# hadolint

> Lints Dockerfiles to help you build [best practice](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices) Docker images.
> More information: https://github.com/hadolint/hadolint.

- Lint a Dockerfile, printing any output to STDOUT:

`hadolint {{Dockerfile}}`

- Lint a Dockerfile ignoring specific rules and outputting JSON:

`hadolint --ignore {{DL3006}} --format json {{Dockerfile}}`

- Lint multiple Dockerfiles while specifying a trusted registry:

`hadolint --trusted-registry {{my.company.com:500}} {{app/Dockerfile}} {{db/Dockerfile}}`
