# trivy

> Scanner for vulnerabilities in container images, file systems, and Git repositories, as well as for configuration issues and hard-coded secrets.
> More information: <https://aquasecurity.github.io/trivy>.

- Scan a Docker image for vulnerabilities:

`trivy image {{alpine:latest}}`

- Scan a Docker image filtering by severities:

`trivy image --severity {{HIGH,CRITICAL}} {{alpine:3.15}}`

- Scan a Docker image ignoring any unfixed/unpatched vulnerabilities:

`trivy image --ignore-unfixed {{alpine:3.15}}`

- Scan a local development project for vulnerabilities:

`trivy fs {{path/to/project}}`

- Scan a remote git repository for vulnerabilities:

`trivy repo {{https://github.com/knqyf263/trivy-ci-test}}`

- Scan a IaC (Terraform, CloudFormation, ARM, Helm and Dockerfile) directory for misconfigurations:

`trivy config {{path/to/directory}}`
