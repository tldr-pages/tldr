#հադոլինտ

> Dockerfile linter.
> Լրացուցիչ տեղեկություններ. <https://github.com/hadolint/hadolint#cli>:.

- Տեղադրեք Dockerfile:

`hadolint {{path/to/Dockerfile}}`

- Տեղադրեք Dockerfile-ը, ցուցադրելով ելքը JSON ձևաչափով.:

`hadolint {{[-f|--format]}} {{json}} {{path/to/Dockerfile}}`

- Տեղադրեք Dockerfile-ը, ելքը ցուցադրելով հատուկ ձևաչափով.:

`hadolint {{[-f|--format]}} {{tty|json|checkstyle|codeclimate|codacy}} {{path/to/Dockerfile}}`

- Տեղադրեք Dockerfile-ը` անտեսելով հատուկ կանոնները.:

`hadolint --ignore {{DL3006}} --ignore {{DL3008}} {{path/to/Dockerfile}}`

- Տեղադրեք բազմաթիվ Dockerfiles՝ օգտագործելով հատուկ վստահելի ռեգիստրներ.:

`hadolint --trusted-registry {{docker.io}} --trusted-registry {{example.com}}:{{5000}} {{path/to/Dockerfile1 path/to/Dockerfile2 ...}}`
