# trivy

> Scanner for vulnerabilities in container images, file systems, and Git repositories, as well as for configuration issues.
> More information: <https://github.com/aquasecurity/trivy>.

- Scan an image:

`trivy image {{image:tag}}`

- Scan the filesystem for vulnerabilities and misconfigurations:

`trivy fs --security-checks {{vuln,config}} {{path/to/project_directory}}`

- Scan a directory for misconfigurations:

`trivy config {{path/to/iac_directory}}`

- Generate output with a SARIF template:

`trivy image --format {{template}} --template {{"@sarif.tpl"}} -o {{path/to/report.sarif}} {{image:tag}}`
