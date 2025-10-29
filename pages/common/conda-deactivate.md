# conda-deactivate

> Deactivate the currently active conda environment.
> When deactivated, your shell will revert to the base or system Python environment.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/deactivate.html>.

- Deactivate the current conda environment:

`conda deactivate`

- Deactivate multiple nested environments (if you have activated environments inside each other):

`conda deactivate && conda deactivate`

- Check the currently active environment before and after deactivation:

`conda info --envs`

- Deactivate and return to the base environment:

`conda deactivate && conda activate base`
