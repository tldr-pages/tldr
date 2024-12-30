# tlmgr

> 管理现有 TeX Live 安装的包和配置选项。
> 一些子命令，如 `paper`，有其自己的使用文档。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 安装一个包及其依赖项：

`tlmgr install {{package}}`

- 移除一个包及其依赖项：

`tlmgr remove {{package}}`

- 显示关于一个包的信息：

`tlmgr info {{package}}`

- 更新所有包：

`tlmgr update --all`

- 显示可用的更新而不更新任何内容：

`tlmgr update --list`

- 启动 tlmgr 的图形用户界面版本：

`tlmgr gui`

- 列出所有 TeX Live 配置：

`tlmgr conf`