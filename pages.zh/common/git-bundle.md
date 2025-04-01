# git bundle

> 将对象和引用打包成存档。
> 更多信息：<https://git-scm.com/docs/git-bundle>.

- 创建包含特定分支所有对象和引用的存档文件：

`git bundle create {{path/to/file.bundle}} {{branch_name}}`

- 创建包含所有分支的存档文件：

`git bundle create {{path/to/file.bundle}} --all`

- 创建包含当前分支最近5次提交的存档文件：

`git bundle create {{path/to/file.bundle}} -5 {{HEAD}}`

- 创建包含最近7天更改的存档文件：

`git bundle create {{path/to/file.bundle}} --since 7.days {{HEAD}}`

- 验证存档文件是否有效，是否可以应用于当前仓库：

`git bundle verify {{path/to/file.bundle}}`

- 将存档文件中包含的引用列表打印到 `stdout`：

`git bundle unbundle {{path/to/file.bundle}}`

- 从存档文件中解包特定分支到当前仓库：

`git pull {{path/to/file.bundle}} {{branch_name}}`

- 从存档创建新仓库：

`git clone {{path/to/file.bundle}}`
