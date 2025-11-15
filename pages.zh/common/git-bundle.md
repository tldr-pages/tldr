# git bundle

> 将对象和引用打包成归档文件。
> 更多信息：<https://git-scm.com/docs/git-bundle>.

- 创建包含特定分支所有对象和引用的打包文件：

`git bundle create {{路径/到/文件.bundle}} {{分支名}}`

- 创建包含所有分支的打包文件：

`git bundle create {{路径/到/文件.bundle}} --all`

- 创建当前分支最近5次提交的打包文件：

`git bundle create {{路径/到/文件.bundle}} -5 {{HEAD}}`

- 创建最近7天提交的打包文件：

`git bundle create {{路径/到/文件.bundle}} --since 7.days {{HEAD}}`

- 验证打包文件是否有效且可应用到当前仓库：

`git bundle verify {{路径/到/文件.bundle}}`

- 显示打包文件中包含的引用列表：

`git bundle unbundle {{路径/到/文件.bundle}}`

- 从打包文件中解包特定分支到当前仓库：

`git pull {{路径/到/文件.bundle}} {{分支名}}`

- 从打包文件创建新仓库：

`git clone {{路径/到/文件.bundle}}`
