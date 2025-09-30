# gcrane

> Container images managing tool.
> This tool implements a superset of the `crane` commands, with additional commands that are specific to `gcr.io`.
> Some subcommands such as `append`, `auth`, `copy`, etc. have their own usage documentation which can be found under `crane`.
> Some subcommands such as `completion`, `gc`, `help` are specific to gcrane and have their own usage documentation.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- List tags, manifests, and sub-repostiories:

`gcrane ls {{gcr.io/${PROJECT_ID}}}`

- Copy images from one registry to another:

`gcrane cp {{[-r|--recursive]}} {{gcr.io/${PROJECT_ID_FROM/repo}}} {{gcr.io/${PROJECT_ID_TO/repo}}}`

- Print images that can be garbage collected:

`gcrane gc {{gcr.io/${PROJECT_ID}/repo}}

- Delete images that can be garbage collected:

`gcrane gc gcr.io/${PROJECT_ID}/repo | xargs -n1 gcrane delete`
