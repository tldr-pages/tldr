# newsboat

> 用于终端的 RSS/Atom 订阅源阅读器。
> 更多信息：<https://newsboat.org/>。

- 首次从 OPML 文件导入订阅源 URL：

`newsboat -i {{my-feeds.xml}}`

- 或者手动添加订阅源：

`echo {{http://example.com/path/to/feed}} >> "${HOME}/.newsboat/urls"`

- 启动 Newsboat 并在启动时刷新所有订阅源：

`newsboat -r`

- 在非交互模式下执行一个或多个命令：

`newsboat -x {{reload print-unread ...}}`

- 查看快捷键（最相关的快捷键在状态栏中可见）：

`<?>`