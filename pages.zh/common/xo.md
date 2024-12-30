# xo

> 一个可插拔的、零配置的JavaScript代码检查工具。
> 更多信息：<https://github.com/xojs/xo>。

- 检查“src”目录中的文件：

`xo`

- 检查一组指定的文件：

`xo {{path/to/file1.js path/to/file2.js ...}}`

- 自动修复发现的任何代码检查问题：

`xo --fix`

- 使用空格作为缩进，而不是制表符：

`xo --space`

- 使用“prettier”代码风格进行检查：

`xo --prettier`