# git lfs

> 在 Git 仓库中处理大文件。
> 更多信息：<https://git-lfs.com>。

- 初始化 Git LFS：

`git lfs install`

- 跟踪匹配通配符的文件：

`git lfs track '{{*.bin}}'`

- 更改 Git LFS 终端 URL（如果 LFS 服务器与 Git 服务器分开，这会很有用）：

`git config {{-f|--file}} .lfsconfig lfs.url {{lfs_endpoint_url}}`

- 列出跟踪的模式：

`git lfs track`

- 列出已提交的跟踪文件：

`git lfs ls-files`

- 将所有 Git LFS 对象推送到远程服务器（如果遇到错误，这会很有用）：

`git lfs push --all {{remote_name}} {{branch_name}}`

- 获取所有 Git LFS 对象：

`git lfs fetch`

- 签出所有 Git LFS 对象：

`git lfs checkout`