# gcrane

> Container images managing tool.
> This tool implements a superset of the `crane` commands, with additional commands that are specific to Google Container Registry (gcr.io).
> Some subcommands such as `append`, `auth`, `copy`, etc. have their own usage documentation which can be found under `crane`.
> Some subcommands such as `completion`, `gc`, `help` are specific to gcrane and have their own usage documentation.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- List tags, manifests, and sub-repostiories:

`gcrane ls {{container_registry}}/{{project_id}}`

- Copy images from one registry to another:

`gcrane cp {{[-r|--recursive]}} {{source_container_registry}}/{{source_project_id}}/{{repository}} {{target_container_registry}}/{{target_project_id}}/{{repository}}`

- Print images that can be garbage collected:

`gcrane gc {{container_registry}}/{{project_id}}/{{repository}}`

- Delete images that can be garbage collected:

`gcrane gc {{container_registry}}/{{project_id}}/{{repository}} | xargs -n1 gcrane delete`
