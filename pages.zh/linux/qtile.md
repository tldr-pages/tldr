# qtile

> 一个功能齐全、可定制的平铺窗口管理器，采用Python编写和配置。
> 更多信息：<https://docs.qtile.org/en/latest/manual/commands/shell/index.html>。

- 启动窗口管理器，如果它还没有运行（理想情况下应该从`.xsession`或类似文件中运行）：

`qtile start`

- 检查配置文件是否有任何编译错误（默认位置是`~/.config/qtile/config.py`）：

`qtile check`

- 显示当前资源使用信息：

`qtile top --force`

- 在名为`test-group`的组中打开程序`xterm`作为浮动窗口：

`qtile run-cmd --group {{test-group}} --float {{xterm}}`

- 重启窗口管理器：

`qtile cmd-obj --object cmd --function restart`