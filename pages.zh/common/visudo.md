# visudo

> 安全编辑 sudoers 文件。
> 更多信息：<https://www.sudo.ws/docs/man/visudo.man>。

- 编辑 sudoers 文件：

`sudo visudo`

- 检查 sudoers 文件是否有错误：

`sudo visudo -c`

- 使用特定编辑器编辑 sudoers 文件：

`sudo EDITOR={{editor}} visudo`

- 显示版本信息：

`visudo --version`