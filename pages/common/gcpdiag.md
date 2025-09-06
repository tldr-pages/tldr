# gcpdiag

> Google Cloud Platform troubleshooting and diagnostics tool.
> Run in a Docker container or in GCP Cloudshell.
> More information: <https://github.com/GoogleCloudPlatform/gcpdiag>.

- Run `gcpdiag` on your project, returning all rules:

`gcpdiag lint --project={{gcp_project_id}}`

- Hide rules that are ok:

`gcpdiag lint --project={{gcp_project_id}} --hide-ok`

- Authenticate using a service account private key file:

`gcpdiag lint --project={{gcp_project_id}} --auth-key {{path/to/private_key}}`

- Search logs and metrics from a number of days back (default: 3 days):

`gcpdiag lint --project={{gcp_project_id}} --within-days {{number}}`

- Display help:

`gcpdiag lint --help`
