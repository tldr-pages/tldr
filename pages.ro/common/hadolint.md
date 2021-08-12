# hadolint

> Linter Dockerfile.
> Mai multe informaţii: <https://github.com/hadolint/hadolint>

- Same un fișier Dockerfile:

`hadolint {{path/to/Dockerfile}}`

- Lint un Dockerfile, afișând ieșirea în format JSON:

`hadolint --format {{json}} {{path/to/Dockerfile}}`

- Lint un Dockerfile, afișând ieșirea într-un format specific:

`hadolint --format {{tty|json|checkstyle|codeclimate|codacy}} {{path/to/Dockerfile}}`

- Same un fișier Dockerfile ignorând regulile specifice:

`hadolint --ignore {{DL3006}} --ignore {{DL3008}} {{path/to/Dockerfile}}`

- Lint mai multe fișiere Dockerfiles folosind registre de încredere specifice:

`hadolint --trusted-registry {{docker.io}} --trusted-registry {{example.com}}:{{5000}} {{path/to/Dockerfile}} {{path/to/another/Dockerfile}}`
