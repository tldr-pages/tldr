# git obliterate

> 从 Git 仓库中删除文件并清除其历史记录。
> 属于 `git-extras`。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-obliterate>。

- 删除特定文件的存在：

`git obliterate {{file_1 file_2 ...}}`

- 在两个提交之间删除特定文件的存在：

`git obliterate {{file_1 file_2 ...}} -- {{commit_hash_1}}..{{commit_hash_2}}`
