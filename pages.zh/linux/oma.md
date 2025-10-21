# oma

> 一款为使用 dpkg 的发行版打造的软件包管理前端。
> 更多信息：<https://github.com/AOSC-Dev/oma#usage>.

- 进入交互式包管理界面：

`sudo oma`

- 安装软件包：

`sudo oma install {{软件包名}}`

- 移除软件包：

`sudo oma remove {{软件包名}}`

- 搜索软件包：

`oma search {{关键词}}`

- 显示软件包的详细信息：

`oma show`

- 将所有已安装的软件包升级至最新版本：

`sudo oma upgrade`

- 更新可用软件包及其版本的列表（执行 `oma install` 和 `oma upgrade` 前会自动执行）：

`sudo oma refresh`

- 查看帮助：

`oma help`
