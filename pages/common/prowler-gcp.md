# prowler gcp

> Assess Google Cloud Platform (GCP) security best practices, audits, and compliance checks.
> See also: `prowler`, `prowler-aws`, `prowler-azure`, `prowler-kubernetes`, `prowler-m365`, `prowler-github`.
> More information: <https://docs.prowler.com/projects/prowler-open-source/en/latest/>.

- Run the default set of checks on all accessible GCP projects using default user credentials:

`prowler gcp`

- Authenticate using a service account credentials file:

`prowler gcp --credentials-file {{path/to/credentials.json}}`

- Scan specific GCP projects by ID:

`prowler gcp --project-ids {{project_id1 project_id2 ...}}`

- Run checks for selected GCP services:

`prowler gcp {{[-s|--services]}} {{iam compute ...}}`

- Run a specific GCP check:

`prowler gcp {{[-c|--checks]}} {{gcp_storage_bucket_logging_enabled}}`

- Exclude specific checks or services:

`prowler gcp {{[-e|--excluded-checks]}} {{gcp_storage_bucket_logging_enabled}} --exclude-services {{iam compute ...}}`
