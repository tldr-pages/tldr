# glab pipeline

> List, view, and run GitLab CI/CD pipelines.
> More information: <https://glab.readthedocs.io/en/latest/pipeline>.

- View a running pipeline on the current branch:

`glab pipeline status`

- View a running pipeline on a specific branch:

`glab pipeline status --branch {{branch_name}}`

- Get the list of pipelines:

`glab pipeline list`

- Run a manual pipeline on the current branch:

`glab pipeline run`

- Run a manual pipeline on a specific branch:

`glab pipeline run --branch {{branch_name}}`
