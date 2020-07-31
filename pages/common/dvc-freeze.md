# dvc freeze

> Freeze stages in DVC pipeline.
> This makes DVC to stop tracking changes in stage dependencies and re-execution untill unfreeze.
> More information: <https://dvc.org/doc/command-reference/freeze>.

- Freeze 1 or more specified stages:

`dvc freeze {{stage_name_a}} [{{stage_name_b}} ...]`

- Unfreeze given stage/s:

`dvc unfreeze {{stage_name/s}}`
