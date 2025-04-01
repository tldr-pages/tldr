# dvc dag

> 可视化 `dvc.yaml` 中定义的管道。
> 更多信息：<https://dvc.org/doc/command-reference/dag>。

- 可视化整个管道：

`dvc dag`

- 可视化到指定目标阶段的管道阶段：

`dvc dag {{target}}`

- 以 dot 格式导出管道：

`dvc dag --dot > {{path/to/pipeline.dot}}`