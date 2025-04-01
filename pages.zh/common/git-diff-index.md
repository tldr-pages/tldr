# git diff-index

> 比较工作目录与某个提交或树对象。
> 更多信息：<https://git-scm.com/docs/git-diff-index>。

- 比较工作目录与特定提交：

`git diff-index {{commit}}`

- 比较工作目录中的特定文件或目录与某个提交：

`git diff-index {{commit}} {{path/to/file_or_directory}}`

- 比较工作目录与索引（暂存区域）以检查已暂存的更改：

`git diff-index --cached {{commit}}`

- 抑制输出并返回退出状态以检查差异：

`git diff-index --quiet {{commit}}`
