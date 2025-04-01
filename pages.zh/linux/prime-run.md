# prime-run

> 使用备用的 Nvidia 显卡运行程序。
> 更多信息：<https://wiki.archlinux.org/title/PRIME#PRIME_渲染卸载>。

- 使用专用的 Nvidia GPU 运行程序：

`prime-run {{command}}`

- 验证是否使用了 Nvidia 显卡：

`prime-run glxinfo | grep "OpenGL renderer"`
