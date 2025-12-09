# gcrane

> Container images managing tool.
> This tool implements a superset of the `crane` commands, with additional commands that are specific to Google Container Registry (`gcr.io`).
> Some subcommands such as `append`, `auth`, `copy`, etc. have their own usage documentation which can be found under `crane`.
> Some subcommands such as `completion`, `gc`, `help` are specific to gcrane and have their own usage documentation.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Login to a registry:

`gcrane auth login {{registry}} {{[-u|--username]}} {{user}} {{[-p|--password]}} {{password}}`

- List tags, manifests, and sub-repostiories:

`gcrane ls {{registry}}/{{project_id}}`

- Copy images from one registry to another:

`gcrane cp {{[-r|--recursive]}} {{source_registry}}/{{project_id}}/{{repository}} {{target_registry}}/{{project_id}}/{{repository}}`

- Print images that can be garbage collected:

`gcrane gc {{registry}}/{{project_id}}/{{repository}}`

- Delete images that can be garbage collected:

`gcrane gc {{registry}}/{{project_id}}/{{repository}} | xargs {{[-n|--max-args]}} 1 gcrane delete`

- List a specific registry with specific ID:

`gcrane ls {{gcr.io}}/{{my-project-id}}`

- Migrate all images from US registry to EU registry:

`gcrane cp {{[-r|--recursive]}} {{gcr.io}}/{{my-project-id}}/{{repository}} {{eu.gcr.io}}/{{my-project-id}}/{{repository}}`
