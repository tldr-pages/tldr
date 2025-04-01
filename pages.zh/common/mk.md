# mk

> 用于执行在 Mkfile 中描述的目标的任务运行器。
> 主要用于从源代码控制可执行文件的编译。
> 更多信息：<https://doc.cat-v.org/plan_9/4th_edition/papers/mk>.

- 调用 Mkfile 中指定的第一个目标（通常名为 "all"）：

`mk`

- 调用特定目标：

`mk {{target}}`

- 调用特定目标，并同时并行执行 4 个任务：

`NPROC=4 mk {{target}}`

- 强制编译目标，即使源文件未更改：

`mk -w{{target}} {{target}}`

- 假定所有目标均已过期。因此，更新 `target` 及其所有依赖项：

`mk -a {{target}}`

- 在出现错误时尽可能继续执行：

`mk -k`