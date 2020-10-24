# dvc dag

> Visualize the pipeline(s) defined in `dvc.yaml`.
> More information: <https://dvc.org/doc/command-reference/dag>.

- Visualize the entire pipeline:

`dvc dag`

- Visualize the pipeline stages up to a specified target stage:

`dvc dag {{target}}`

- Export the pipeline in the dot format:

`dvc dag --dot > {{path/to/pipeline.dot}}`
