# git diff-index

> 比较工作目录与一个提交或树对象。
> 更多信息：<https://git-scm.com/docs/git-diff-index>。

- 将工作目录与特定提交进行比较：

`git diff-index {{commit}}`

- 将工作目录中特定文件或目录与提交进行比较：

`git diff-index {{commit}} {{path/to/file_or_directory}}`

- 将工作目录与索引（暂存区）进行比较，以检查暂存的更改：

`git diff-index --cached {{commit}}`

- 抑制输出并返回退出状态以检查差异：

`git diff-index --quiet {{commit}}`