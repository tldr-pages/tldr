# dvc freeze

> Freeze stages in the DVC pipeline.
> This prevents DVC from tracking changes in stage dependencies and re-execution until unfreeze.
> See also `dvs unfreeze`.
> More information: <https://dvc.org/doc/command-reference/freeze>.

- Freeze 1 or more specified stages:

`dvc freeze {{stage_name_a}} [{{stage_name_b}} ...]`
