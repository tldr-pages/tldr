# prowler

> Performs security best practices assessments, audits and compliance checks across AWS, Azure, Google Cloud, and Kubernetes.
> See also: `prowler-aws`, `prowler-azure`, `prowler-gcp`, `prowler-kubernetes`, `prowler-m365`, `prowler-github`.
> More information: <https://docs.prowler.com/projects/prowler-open-source/en/latest/>.

- Run an AWS, Azure, GCP, Kubernetes - as provider - audit with default checks:

`prowler {{provider}}`

- Show all available checks for a specific provider:

`prowler {{provider}} {{[-l|--list-checks]}}`

- Show all available services for a specific provider:

`prowler {{provider}} --list-services`

- Generate output in multiple formats, including JSON-ASFF for AWS Security Hub:

`prowler {{provider}} --output-modes {{csv,json-asff,html,...}}`

- Execute in verbose mode:

`prowler {{provider}} --verbose`

- Filter findings by status:

`prowler {{provider}} --status {{PASS,FAIL,MANUAL}}`

- Display help:

`prowler --help`

- Display version:

`prowler {{[-v|--version]}}`
