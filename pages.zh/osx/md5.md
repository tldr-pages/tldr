# md5

> 计算 MD5 加密校验和。
> 更多信息：<https://keith.github.io/xcode-man-pages/md5.1.html>。

- 计算文件的 MD5 校验和：

`md5 {{path/to/file}}`

- 计算多个文件的 MD5 校验和：

`md5 {{path/to/file1 path/to/file2 ...}}`

- 只输出 MD5 校验和（不显示文件名）：

`md5 -q {{path/to/file}}`

- 打印给定字符串的校验和：

`md5 -s "{{string}}"`