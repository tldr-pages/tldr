# git obliterate

> 从 Git 仓库中删除文件并抹去它们的历史记录。
> 是 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-obliterate>。

- 抹去特定文件的存在：

`git obliterate {{file_1 file_2 ...}}`

- 在两个提交之间抹去特定文件的存在：

`git obliterate {{file_1 file_2 ...}} -- {{commit_hash_1}}..{{commit_hash_2}}`