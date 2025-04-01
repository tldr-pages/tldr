# dvc freeze

> 在 DVC 管道中冻结阶段。
> 这会阻止 DVC 跟踪阶段依赖项的变化和重新执行，直到解冻。
> 参见 `dvc unfreeze`。
> 更多信息：<https://dvc.org/doc/command-reference/freeze>。

- 冻结一个或多个指定的阶段：

`dvc freeze {{stage_name1 stage_name2 ...}}`