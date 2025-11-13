# prowler aws

> Assess AWS security best practices, perform audits, compliance checks, and generate reports.
> See also: `prowler`, `prowler-azure`, `prowler-gcp`, `prowler-kubernetes`, `prowler-m365`, `prowler-github`.
> More information: <https://docs.prowler.com/projects/prowler-open-source/en/latest/>.

- Run the default set of checks on the AWS account:

`prowler aws`

- Use a custom AWS profile and filter audited regions:

`prowler aws {{[-p|--profile]}} {{custom-profile}} {{[-f|--filter-region]}} {{us-east-1 eu-south-2 ...}}`

- Run checks for selected AWS services:

`prowler aws {{[-s|--services]}} {{s3|ec2|...}}`

- Run a specific AWS check:

`prowler aws {{[-c|--checks]}} {{s3_bucket_public_access}}`

- Exclude specific checks or services:

`prowler aws {{[-e|--excluded-checks]}} {{s3_bucket_public_access}} --exclude-services {{s3|ec2|...}}`
