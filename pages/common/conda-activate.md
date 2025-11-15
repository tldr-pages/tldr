# conda activate

> Activate a conda environment.
> See also: `conda deactivate` to deactivate a conda environment.
> More information: <https://docs.conda.io/projects/conda/en/stable/dev-guide/deep-dives/activation.html>.

- Activate an existing environment named `myenv`:

`conda activate myenv`

- Activate an existing environment located at custom path:

`conda activate {{path/to/myenv}}`

- Stack `myenv` environment on top of a previous environment making libraries/commands/variables from both accessible:

`conda activate --stack myenv`

- Start a clean environment `myenv` without stacking it making previous environment libraries/commands/variables not accessible:

`conda activate --no-stack myenv`

- Display help:

`conda activate {{[-h|--help]}}`
