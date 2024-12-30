# grub-script-check

> 程序 `grub-script-check` 接受一个 GRUB 脚本文件并检查其语法错误。
> 它可以将路径作为非选项参数。如果没有提供路径，它将从 `stdin` 读取。
> 更多信息请访问：<https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dscript_002dcheck.html>。

- 检查特定脚本文件的语法错误：

`grub-script-check {{path/to/grub_config_file}}`

- 在读取输入后显示每一行：

`grub-script-check --verbose`

- 显示帮助信息：

`grub-script-check --help`

- 显示版本信息：

`grub-script-check --version`