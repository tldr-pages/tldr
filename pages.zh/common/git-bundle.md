# git bundle

> 将对象和引用打包成一个归档文件。
> 更多信息：<https://git-scm.com/docs/git-bundle>。

- 创建一个包含特定分支所有对象和引用的捆绑文件：

`git bundle create {{path/to/file.bundle}} {{branch_name}}`

- 创建一个包含所有分支的捆绑文件：

`git bundle create {{path/to/file.bundle}} --all`

- 创建一个包含当前分支最后 5 次提交的捆绑文件：

`git bundle create {{path/to/file.bundle}} -5 {{HEAD}}`

- 创建一个包含最近 7 天的捆绑文件：

`git bundle create {{path/to/file.bundle}} --since 7.days {{HEAD}}`

- 验证捆绑文件是否有效，并且可以应用到当前的仓库：

`git bundle verify {{path/to/file.bundle}}`

- 将捆绑文件中包含的引用列表打印到 `stdout`：

`git bundle unbundle {{path/to/file.bundle}}`

- 从捆绑文件中将特定分支解包到当前仓库：

`git pull {{path/to/file.bundle}} {{branch_name}}`

- 从捆绑文件创建一个新仓库：

`git clone {{path/to/file.bundle}}`