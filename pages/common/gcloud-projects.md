# gcloud projects

> Manage project access policies in Google Cloud.
> See also: `gcloud`.
> More information: <https://cloud.google.com/sdk/gcloud/reference/projects>.

- Create a new project:

`gcloud projects create {{project_id|project_number}}`

- List all active projects:

`gcloud projects list`

- Display metadata for a project:

`gcloud projects describe {{project_id}}`

- Delete a project:

`gcloud projects delete {{project_id|project_number}}`

- Add an IAM policy binding to a specified project:

`gcloud projects add-iam-policy-binding {{project_id}} --member {{principal}} --role {{role}}`
