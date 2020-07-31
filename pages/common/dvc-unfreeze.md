# dvc unfreeze

> Unfreeze stages in the DVC pipeline.
> This allows DVC to start tracking changes in stage dependencies again after they were frozen.
> See also `dvc freeze`.
> More information: <https://dvc.org/doc/command-reference/unfreeze>.

- Unfreeze given stage/s:

`dvc unfreeze {{stage_name_a}} [{{stage_name_b}} ...]`

- Freeze given stage/s:

`dvc freeze {{stage_name/s}}`
