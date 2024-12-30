# pinky

> 使用 `finger` 协议打印用户信息。
> 更多信息：<https://manned.org/pinky>。

- 显示当前用户的详细信息：

`pinky`

- 显示特定用户的详细信息：

`pinky {{user}}`

- 以长格式显示详细信息：

`pinky {{user}} -l`

- 在长格式中省略用户的主目录和 shell：

`pinky {{user}} -lb`

- 在长格式中省略用户的项目文件：

`pinky {{user}} -lh`

- 在短格式中省略列标题：

`pinky {{user}} -f`