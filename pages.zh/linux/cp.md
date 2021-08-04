# cp

> 复制文件和目录。
> 更多信息：<https://www.gnu.org/software/coreutils/cp>.

- 复制一个文件到另外一个地方：

`cp {{path/to/source_file.ext}} {{path/to/target_file.ext}}`

- 复制一个文件到另外一个目录, 保持文件名不变：

`cp {{path/to/source_file.ext}} {{path/to/target_parent_directory}}`

- 递归的复制一个目录内的内容到另外一个地方（如果目标目录存在，目录被复制到目标目标内部）：

`cp -r {{path/to/source_directory}} {{path/to/target_directory}}`

- 以详细模式递归的复制一个目录 (当文件被复制的时候显示)：

`cp -vr {{path/to/source_directory}} {{path/to/target_directory}}`

- 以交互模式复制文本文件到另外一个地方（在覆盖之前提示用户）：

`cp -i {{*.txt}} {{path/to/target_directory}}`

- 跟踪软连接复制：

`cp -L {{link}} {{path/to/target_directory}}`

- 使用原始文件的全路径，在复制的时候目录不存在则离开创建：

`cp --parents {{source/path/to/file}} {{path/to/target_file}}`
