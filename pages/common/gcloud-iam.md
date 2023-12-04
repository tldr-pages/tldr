# gcloud iam

> Configure Identity and Access Management (IAM) preferences and service accounts.
> More information: <https://cloud.google.com/sdk/docs/cheatsheet#iam>.

- List IAM grantable roles for a resource:

`gcloud iam list-grantable-roles`

- Create a custom role for a project or organization:

`gcloud iam roles create`

- Create a service account for a project:

`gcloud iam service-accounts create`

- Add an IAM policy binding to a service account:

`gcloud iam service-accounts add-iam-policy-binding`

- Replace existing IAM policy binding:

`gcloud iam service-accounts set-iam-policy-binding`

- List a service account's keys:

`gcloud iam service-accounts keys list`
