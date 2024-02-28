# checkov

> Checkov is a static code analysis tool for infrastructure as code (IaC).
> It is also a software composition analysis (SCA) tool for images and open source packages.
> More information: <https://www.checkov.io/1.Welcome/Quick%20Start.html>.

- Scan a directory containing IaC code (Terraform, Cloudformation, arm, Ansible, Bicep, Dockerfile, etc):

`checkov --directory {{path/to/IaC_dir}}`

- Scan a IaC file and omit any code block in output:

`checkov --compact --file {{path/to/iac_code_file}}`

- List all checks for all IaC types:

`checkov --list`
