# dvc dag

> Visualize the pipeline(s) in dvc.yaml
> More information: <https://dvc.org/doc/command-reference/dag>.

- Visualize entire pipeline:

`dvc dag`

- Visualize pipeline stages up to a target stage:

`dvc dag {{target}}`

- Export pipeline in dot format:

`dvc dag --dot > pipeline.dot`

- Export pipeline as SVG:

`dvc dag --dot | dot -Tsvg -o pipeline.svg`
