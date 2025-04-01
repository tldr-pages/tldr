# dvc unfreeze

> 解冻 DVC 流水线中的阶段。
> 这允许 DVC 在阶段依赖被冻结后重新开始跟踪这些依赖的变化。
> 有关更多信息，请参见 `dvc freeze`。
> 更多信息：<https://dvc.org/doc/command-reference/unfreeze>.

- 解冻一个或多个指定的阶段：

`dvc unfreeze {{stage_name1 stage_name2 ...}}`
