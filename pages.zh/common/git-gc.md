# git gc

> 通过清理不必要的文件来优化本地仓库。
> 更多信息：<https://git-scm.com/docs/git-gc>。

- 优化仓库：

`git gc`

- 进行激进优化，耗时更长：

`git gc --aggressive`

- 不清理松散对象（默认会清理）：

`git gc --no-prune`

- 抑制所有输出：

`git gc --quiet`

- 显示帮助：

`git gc --help`