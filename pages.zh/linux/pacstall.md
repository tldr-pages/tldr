# pacstall

> 一个适用于 Ubuntu 的 AUR 软件包管理器。
> 更多信息：<https://github.com/pacstall/pacstall>。

- 在软件包数据库中搜索软件包名称：

`pacstall --search {{query}}`

- 安装软件包：

`pacstall --install {{package}}`

- 卸载软件包：

`pacstall --remove {{package}}`

- 将仓库添加到数据库（仅支持 GitHub 和 GitLab）：

`pacstall --add-repo {{remote_repository_location}}`

- 更新 pacstall 的脚本：

`pacstall --update`

- 更新所有软件包：

`pacstall --upgrade`

- 显示软件包的信息：

`pacstall --cache-info {{package}}`

- 列出所有已安装的软件包：

`pacstall --list`
