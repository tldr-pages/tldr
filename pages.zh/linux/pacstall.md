# pacstall

> 一个用于 Ubuntu 的 AUR 包管理器。
> 更多信息：<https://github.com/pacstall/pacstall>。

- 在包数据库中搜索包名：

`pacstall --search {{query}}`

- 安装一个包：

`pacstall --install {{package}}`

- 移除一个包：

`pacstall --remove {{package}}`

- 向数据库添加一个仓库（仅支持 GitHub 和 GitLab）：

`pacstall --add-repo {{remote_repository_location}}`

- 更新 pacstall 的脚本：

`pacstall --update`

- 更新所有包：

`pacstall --upgrade`

- 显示有关包的信息：

`pacstall --cache-info {{package}}`

- 列出所有已安装的包：

`pacstall --list`