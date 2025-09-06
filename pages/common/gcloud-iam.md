# gcloud iam

> Configure Identity and Access Management (IAM) preferences and service accounts.
> See also: `gcloud`.
> More information: <https://cloud.google.com/sdk/gcloud/reference/iam>.

- List IAM grantable roles for a resource:

`gcloud iam list-grantable-roles {{resource}}`

- Create a custom role for a organization or project:

`gcloud iam roles create {{role_name}} --{{organization|project}} {{organization|project_id}} --file {{path/to/role.yaml}}`

- Create a service account for a project:

`gcloud iam service-accounts create {{name}}`

- Add an IAM policy binding to a service account:

`gcloud iam service-accounts add-iam-policy-binding {{service_account_email}} --member {{member}} --role {{role}}`

- Replace existing IAM policy binding:

`gcloud iam service-accounts set-iam-policy {{service_account_email}} {{policy_file}}`

- List a service account's keys:

`gcloud iam service-accounts keys list --iam-account {{service_account_email}}`
