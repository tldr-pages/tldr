# git sparse-checkout

> 仅检出仓库的部分文件，而不是克隆或检出全部文件（稀疏检出）。
> 更多信息：<https://manned.org/git-sparse-checkout>.

- 启用稀疏检出：

`git sparse-checkout init`

- 禁用稀疏检出并恢复完整仓库：

`git sparse-checkout disable`

- 指定要包含的目录（或文件）：

`git sparse-checkout set {{路径/到/文件或目录}}`

- 稍后添加更多路径：

`git sparse-checkout add {{路径/到/文件或目录}}`
