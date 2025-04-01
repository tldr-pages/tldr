# qtile

> 一个功能齐全且可修改的平铺式窗口管理器，使用 Python 编写和配置。
> 更多信息：<https://docs.qtile.org/en/latest/manual/commands/shell/index.html>.

- 如果窗口管理器尚未运行，则启动它（理想情况下应从 `.xsession` 或类似的文件中运行）：

`qtile start`

- 检查配置文件中的任何编译错误（默认位置是 `~/.config/qtile/config.py`）：

`qtile check`

- 显示当前的资源使用情况信息：

`qtile top --force`

- 在名为 `test-group` 的组中以浮动窗口方式打开 `xterm` 程序：

`qtile run-cmd --group {{test-group}} --float {{xterm}}`

- 重新启动窗口管理器：

`qtile cmd-obj --object cmd --function restart`