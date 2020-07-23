# dvc freeze

> Freeze stages in DVC pipeline.
> This makes DVC to stop tracking changes in stage dependencies and re-execution untill unfreeze.
> More information: <https://dvc.org/doc/command-reference/freeze>.

- Freeze given stage/s:

`dvc freeze {{stage_name/s}}`

- Unfreeze given stage/s:

`dvc unfreeze {{stage_name/s}}`
