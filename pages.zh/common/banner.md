# banner

> 将给定参数输出为大型 ASCII 文字。
> 更多信息：<https://manned.org/banner>.

- 将文字信息打印为大横幅（引号是可选的）：

`banner "{{Hello World}}"`

- 将文字信息打印为横幅，宽度为 50 个字：

`banner -w {{50}} "{{Hello World}}"`

- 从 `stdin` 中读取文本：

`banner`
