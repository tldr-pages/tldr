# dockutil

> 管理 macOS Dock 项目。
> 更多信息：<https://github.com/kcrawford/dockutil>。

- 将应用程序添加到当前用户的 Dock 末尾：

`dockutil --add {{path/to/application}}`

- 在当前用户的 Dock 中用另一个应用程序替换一个应用程序：

`dockutil --add {{/path/to/application}} --replacing '{{dock_item_label}}'`

- 添加一个目录，并设置查看选项，将其显示为文件夹图标或堆叠：

`dockutil --add {{/path/to/directory}} --view {{grid|fan|list|auto}} --display {{folder|stack}}`

- 在另一个项目后添加一个 URL Dock 项：

`dockutil --add {{vnc://example_server.local}} --label '{{Example VNC}}' --after {{dock_item_label}}`

- 根据 Dock 标签名称从 Dock 中移除一个应用程序：

`dockutil --remove '{{dock_item_label}}'`

- 在应用程序后面添加一个间隔：

`dockutil --add '' --type {{spacer|small-spacer|flex-spacer}} --section {{apps}} --after {{dock_item_label}}`

- 移除所有间隔图块：

`dockutil --remove spacer-tiles`