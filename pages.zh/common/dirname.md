# dirname

> 从路径中移除尾部的文件名部分。
> 另请参阅：`basename`。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/dirname-invocation.html>。

- 计算给定路径的父目录：

`dirname {{路径/到/文件或目录}}`

- 计算多个路径的父目录：

`dirname {{路径/到/文件或目录1 路径/到/文件或目录2 ...}}`

- 使用 NUL 字符而非换行符分隔输出（与 `xargs` 结合使用时很有用）：

`dirname {{[-z|--zero]}} {{路径/到/文件或目录1 路径/到/文件或目录2 ...}}`
