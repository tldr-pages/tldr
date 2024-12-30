# git mr

> 本地检出 GitLab 合并请求。
> 这是 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-mr>。

- 检出特定的合并请求：

`git mr {{mr_number}}`

- 从特定的远程检出合并请求：

`git mr {{mr_number}} {{remote}}`

- 从其 URL 检出合并请求：

`git mr {{url}}`

- 清理旧的合并请求分支：

`git mr clean`