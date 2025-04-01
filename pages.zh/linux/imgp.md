# imgp

> 命令行图像调整大小和旋转工具，支持JPEG和PNG图像。
> 更多信息：<https://github.com/jarun/imgp>。

- 转换单个图像和/或包含有效图像格式的整个目录：

`imgp -x {{1366x1000}} {{path/to/directory}} {{path/to/file}}`

- 将图像缩小到75%并覆盖源图像到目标分辨率：

`imgp -x {{75}} -w {{path/to/file}}`

- 将图像顺时针旋转90度：

`imgp -o {{90}} {{path/to/file}}`
