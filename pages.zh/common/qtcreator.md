# qtcreator

> 跨平台的 Qt 应用程序 IDE。
> 更多信息：<https://doc.qt.io/qtcreator/creator-cli.html>。

- 启动 Qt Creator：

`qtcreator`

- 启动 Qt Creator 并恢复上一个会话：

`qtcreator -lastsession`

- 启动 Qt Creator，但不加载指定的插件：

`qtcreator -noload {{plugin}}`

- 启动 Qt Creator，但不加载任何插件：

`qtcreator -noload {{all}}`

- 以演示模式启动 Qt Creator，并显示键盘快捷键的弹出提示：

`qtcreator -presentationMode`

- 启动 Qt Creator 并显示特定提交的差异：

`qtcreator -git-show {{commit}}`