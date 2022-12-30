# gcpdiag

> Google Cloud Platform troubleshooting and diagnostics tool.
> Run in a docker container or in GCP Cloudshell.
> More information: <https://github.com/GoogleCloudPlatform/gcpdiag>.

- Run `gcpdiag` on specific project, returning all rules:

`gcpdiag lint --project="{{id}}"`

- Hide rules that are ok:

`gcpdiag lint --project="{{id}}" --hide-ok`

- Authenticate using a specific service account private key file:

`gcpdiag lint --project="{{id}}" --auth-key {{path/to/private_key}}`

- Search logs and metrics from a number of days back (default: 3 days):

`gcpdiag lint --project="{{id}}" --within-days {{1..infinity}}`

- Display help:

`gcpdiag lint --help`
