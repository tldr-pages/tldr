# newsboat

> 一款用于文本终端的RSS/Atom订阅阅读器。
> 更多信息请访问：<https://newsboat.org/>.

- 首先从OPML文件导入订阅网址：

`newsboat -i {{my-feeds.xml}}`

- 或者，手动添加订阅：

`echo {{http://example.com/path/to/feed}} >> "${HOME}/.newsboat/urls"`

- 启动Newsboat并在启动时刷新所有订阅：

`newsboat -r`

- 在非交互模式下执行一个或多个命令：

`newsboat -x {{reload print-unread ...}}`

- 查看键盘快捷键（最相关的快捷键在状态栏中可见）：

`?`