# prime-run

> 使用备用的Nvidia显卡运行程序。
> 更多信息：<https://wiki.archlinux.org/title/PRIME#PRIME_render_offload>。

- 使用专用的Nvidia GPU运行程序：

`prime-run {{command}}`

- 验证是否正在使用Nvidia显卡：

`prime-run glxinfo | grep "OpenGL renderer"`