# trivy

> Scanner for vulnerabilities in container images, file systems, and Git repositories, as well as for configuration issues.
> More information: <https://aquasecurity.github.io/trivy>.

- Scan a Docker image for vulnerabilities and exposed secrets:

`trivy image {{image:tag}}`

- Scan a Docker image filtering the output by severity:

`trivy image --severity {{HIGH,CRITICAL}} {{alpine:3.15}}`

- Scan a Docker image ignoring any unfixed/unpatched vulnerabilities:

`trivy image --ignore-unfixed {{alpine:3.15}}`

- Scan the filesystem for vulnerabilities and misconfigurations:

`trivy fs --security-checks {{vuln,config}} {{path/to/project_directory}}`

- Scan a IaC (Terraform, CloudFormation, ARM, Helm and Dockerfile) directory for misconfigurations:

`trivy config {{path/to/iac_directory}}`

- Scan a local or remote Git repository for vulnerabilities:

`trivy repo {{path/to/local_repository_directory|remote_repository_URL}}`

- Scan a Git repository up to a specific commit hash:

`trivy repo --commit {{commit_hash}} {{repository}}`

- Generate output with a SARIF template:

`trivy image --format {{template}} --template {{"@sarif.tpl"}} -o {{path/to/report.sarif}} {{image:tag}}`
