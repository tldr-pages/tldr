# hadolint

> Dockerfile linter. További információ: <https://github.com/hadolint/hadolint>.

- Dockerfile linterezése:

`hadolint {{path/to/Dockerfile}}`

- Egy Dockerfile foltozása, a kimenet JSON formátumban történő megjelenítésével:

`hadolint --format {{json}} {{path/to/Dockerfile}}`

- Lint a Dockerfile, a kimenet megjelenítésével egy adott formátumban:

`hadolint --format {{tty|json|checkstyle|codeclimate|codacy}} {{path/to/Dockerfile}}`

- Dockerfile futtatása bizonyos szabályok figyelmen kívül hagyásával:

`hadolint --ignore {{DL3006}} --ignore {{DL3008}} {{path/to/Dockerfile}}`

- Több Dockerfile futtatása bizonyos megbízható regiszterek használatával:

`hadolint --trusted-registry {{docker.io}} --trusted-registry {{example.com}}:{{5000}} {{path/to/Dockerfile}} {{path/to/another/Dockerfile}}`
