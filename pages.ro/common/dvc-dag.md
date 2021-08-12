# dvc dag

> Vizualizaţi conducta (conductele) definită (definite) în `dvc.yaml`.
> Mai multe informaţii: <https://dvc.org/doc/command-reference/dag>

- Vizualizaţi întreaga conductă:

`dvc dag`

- Vizualizarea etapelor conductei până la o etapă țintă specificată:

`dvc dag {{target}}`

- Exportați conducta în format punct:

`dvc dag --dot > {{path/to/pipeline.dot}}`
