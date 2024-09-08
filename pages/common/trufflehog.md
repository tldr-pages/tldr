# trufflehog

> Find and verify credentials in files, Git repositories, S3 buckets, and Docker images.
> More information: <https://github.com/trufflesecurity/trufflehog>.

- Scan a Git repository for verified secrets:

`trufflehog git {{https://github.com/trufflesecurity/test_keys}} --only-verified`

- Scan a GitHub organization for verified secrets:

`trufflehog github --org={{trufflesecurity}} --only-verified`

- Scan a GitHub repository for verified keys and get JSON output:

`trufflehog git {{https://github.com/trufflesecurity/test_keys}} --only-verified --json`

- Scan a GitHub repository along with its Issues and Pull Requests:

`trufflehog github --repo={{https://github.com/trufflesecurity/test_keys}} --issue-comments --pr-comments`

- Scan an S3 bucket for verified keys:

`trufflehog s3 --bucket={{bucket name}} --only-verified`

- Scan S3 buckets using IAM Roles:

`trufflehog s3 --role-arn={{iam-role-arn}}`

- Scan individual files or directories:

`trufflehog filesystem {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Scan a Docker image for verified secrets:

`trufflehog docker --image {{trufflesecurity/secrets}} --only-verified`
