# mk

> Mkfile中描述的目标的任务运行器。
> 主要用于控制从源代码编译可执行文件的过程。
> 更多信息：<https://doc.cat-v.org/plan_9/4th_edition/papers/mk>。

- 调用Mkfile中指定的第一个目标（通常命名为“all”）：

`mk`

- 调用特定目标：

`mk {{target}}`

- 调用特定目标，同时并行执行4个作业：

`NPROC=4 mk {{target}}`

- 强制生成一个目标，即使源文件没有更改：

`mk -w{{target}} {{target}}`

- 假设所有目标都过时。因此，更新`target`及其所有依赖项：

`mk -a {{target}}`

- 在出错时尽可能继续：

`mk -k`