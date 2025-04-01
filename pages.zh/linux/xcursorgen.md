# xcursorgen

> 从一组 PNG 图像文件创建 X 光标文件。
> 如果省略 `--prefix`，图像文件必须位于当前工作目录中。
> 更多信息：<https://manned.org/xcursorgen>。

- 使用配置文件创建 X 光标文件：

`xcursorgen {{path/to/config.cursor}} {{path/to/output_file}}`

- 使用配置文件创建 X 光标文件，并指定图像文件的路径：

`xcursorgen --prefix {{path/to/image_directory/}} {{path/to/config.cursor}} {{path/to/output_file}}`

- 使用配置文件创建 X 光标文件，并将输出写入 `stdout`：

`xcursorgen {{path/to/config.cursor}}`
