# localectl

> 控制系统的语言环境和键盘布局设置。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/localectl.html>。

- 显示当前系统的语言环境和键盘映射设置：

`localectl`

- 列出可用的语言环境：

`localectl list-locales`

- 设置系统语言环境变量：

`localectl set-locale {{LANG}}={{en_US.UTF-8}}`

- 列出可用的键盘映射：

`localectl list-keymaps`

- 为控制台和 X11 设置系统键盘映射：

`localectl set-keymap {{us}}`
