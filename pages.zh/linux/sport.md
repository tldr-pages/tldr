# sport

> 搜索和安装 SlackBuilds。
> 更多信息：<http://slackermedia.info/handbook/doku.php?id=slackbuilds>.

- 首次运行 `sport` 时，拉取 SlackBuilds 列表：

`sudo mkdir -p /usr/ports && sudo rsync -av rsync://slackbuilds.org /slackbuilds/$(awk '{print $2}' /etc/slackware-version)/ /usr/ports/`

- 通过 `rsync` 拉取系统树的更新：

`sudo sport rsync`

- 按名称搜索软件包：

`sport search "{{keyword}}"`

- 检查软件包是否已安装：

`sport check {{package}}`

- 显示软件包的 README 和 `.info` 文件：

`sport cat {{package}}`

- 解决依赖关系后安装软件包：

`sudo sport install {{package}}`

- 从文件中安装一列软件包（格式：软件包之间用空格分隔）：

`sudo sport install $(< {{path/to/list}})`
