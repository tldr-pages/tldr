# dockutil

> 管理 macOS Dock 项目。
> 更多信息：<https://github.com/kcrawford/dockutil>.

- 在当前用户的 Dock 末尾添加一个应用程序：

`dockutil --add {{path/to/application}}`

- 在当前用户的 Dock 中用一个应用程序替换另一个应用程序：

`dockutil --add {{/path/to/application}} --replacing '{{dock_item_label}}'`

- 添加一个目录，并设置视图选项，显示为文件夹图标或堆栈：

`dockutil --add {{/path/to/directory}} --view {{grid|fan|list|auto}} --display {{folder|stack}}`

- 在另一个项目之后添加一个 URL Dock 项目：

`dockutil --add {{vnc://example_server.local}} --label '{{Example VNC}}' --after {{dock_item_label}}`

- 根据 Dock 项目的标签名称从 Dock 中移除一个应用程序：

`dockutil --remove '{{dock_item_label}}'`

- 在某个应用程序之后的某个部分添加一个分隔符：

`dockutil --add '' --type {{spacer|small-spacer|flex-spacer}} --section {{apps}} --after {{dock_item_label}}`

- 移除所有分隔符图标：

`dockutil --remove spacer-tiles`