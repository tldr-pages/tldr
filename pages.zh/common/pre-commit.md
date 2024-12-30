# pre-commit

> 创建在提交之前运行的 Git 钩子。
> 更多信息：<https://pre-commit.com>。

- 将 pre-commit 安装到你的 Git 钩子中：

`pre-commit install`

- 在所有已暂存文件上运行 pre-commit 钩子：

`pre-commit run`

- 在所有文件上运行 pre-commit 钩子，无论是已暂存的还是未暂存的：

`pre-commit run --all-files`

- 清理 pre-commit 缓存：

`pre-commit clean`