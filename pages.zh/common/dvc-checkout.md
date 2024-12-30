# dvc checkout

> 从缓存中检出数据文件和目录。
> 更多信息：<https://dvc.org/doc/command-reference/checkout>。

- 检出所有目标文件和目录的最新版本：

`dvc checkout`

- 检出指定目标的最新版本：

`dvc checkout {{target}}`

- 从不同的 Git 提交/标签/分支检出目标的特定版本：

`git checkout {{commit_hash|tag|branch}} {{target}} && dvc checkout {{target}}`