# dvc freeze

> Freeze stages in the DVC pipeline.
> This prevents DVC from tracking changes in stage dependencies and re-execution until unfreeze.
> See also: `dvc unfreeze`.
> More information: <https://doc.dvc.org/command-reference/freeze>.

- Freeze one or more specified stages:

`dvc freeze {{stage_name1 stage_name2 ...}}`
