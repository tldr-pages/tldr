# 横幅

> 将参数以大ASCII艺术形式打印。
> 更多信息：<https://manned.org/banner>。

- 将文本消息打印为大横幅（引号为可选）：

`banner "{{Hello World}}"`

- 使用50个字符的横幅[w]idth：

`banner -w 50 "{{Hello World}}"`

- 从`stdin`读取文本：

`banner`