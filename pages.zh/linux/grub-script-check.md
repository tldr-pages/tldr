# grub-script-check

> 程序 `grub-script-check` 用于检查 GRUB 脚本文件的语法错误。
> 它可以接受一个非选项参数作为路径。如果没有提供路径，它将从 `stdin` 读取。
> 更多信息：<https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dscript_002dcheck.html>.

- 检查特定脚本文件的语法错误：

`grub-script-check {{path/to/grub_config_file}}`

- 读取输入后显示每一行：

`grub-script-check {{[-v|--verbose]}}`

- 显示帮助信息：

`grub-script-check --help`

- 显示版本信息：

`grub-script-check --version`