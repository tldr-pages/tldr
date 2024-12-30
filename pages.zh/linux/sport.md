# sport

> 搜索并安装 SlackBuilds。
> 更多信息: <http://slackermedia.info/handbook/doku.php?id=slackbuilds>。

- 首次运行 `sport` 以拉取 SlackBuilds 列表：

`sudo mkdir -p /usr/ports && sudo rsync -av rsync://slackbuilds.org /slackbuilds/$(awk '{print $2}' /etc/slackware-version)/ /usr/ports/`

- 通过 `rsync` 拉取系统树的任何更新：

`sudo sport rsync`

- 按名称搜索包：

`sport search "{{keyword}}"`

- 检查包是否已安装：

`sport check {{package}}`

- 显示包的 README 和 `.info` 文件：

`sport cat {{package}}`

- 在解决依赖关系后安装包：

`sudo sport install {{package}}`

- 从文件中安装包列表（格式：用空格分隔的包）：

`sudo sport install $(< {{path/to/list}})`