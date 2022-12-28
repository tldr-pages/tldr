# gcpdiag

> Google Cloud Platform troubleshooting and diagnostics tool.
> Run in a docker container or in GCP Cloudshell.
> More information: <https://github.com/GoogleCloudPlatform/gcpdiag>.

- Run `gcpdiag` on your project, returning all rules:

`gcpdiag lint --project={{gcp_project_id}}`

- Hide rules that are ok:

`gcpdiag lint --project={{GCP Project ID}} --hide-ok`

- Runs gcpdiag on your project and authenticate using a service account private key file:

`gcpdiag lint --project={{gcp_project_id}} --auth-key {{path/to/private_key}}`

- Runs gcpdiag on your project, searching logs and metric from {{number}} of days back (default: 3 days):

`gcpdiag lint --project={{GCP Project ID}} --within-days {{number}}`

- Shows the full command options and flags of gcpdiag:

`gcpdiag lint --help`
