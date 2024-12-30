# dvc init

> 初始化一个新的本地 DVC 仓库。
> 更多信息：<https://dvc.org/doc/command-reference/init>。

- 初始化一个新的本地仓库：

`dvc init`

- 在没有 Git 的情况下初始化 DVC：

`dvc init --no-scm`

- 在子目录中初始化 DVC：

`cd {{path/to/subdir}} && dvc init --sudir`