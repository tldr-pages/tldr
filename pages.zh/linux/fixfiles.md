# 修复文件

> 修复文件的SELinux安全上下文。
> 更多信息请访问: <https://manned.org/fixfiles>。

- 如果与onboot一起指定，fixfiles将记录当前日期到`/.autorelabel`文件中，以便在以后加速标签。如果与restore一起使用，restore将仅影响今天修改的文件：

`fixfiles -B`

- [F]orce将上下文重置为与可自定义文件的`file_context`匹配：

`fixfiles -F`

- 在不确认的情况下清空`/tmp`目录：

`fixfiles -f`

- 使用[R]pm数据库发现特定包中的所有文件并恢复文件上下文：

`fixfiles -R {{rpm_package1,rpm_package2 ...}}`

- 对`PREVIOUS_FILECONTEXT`文件与[现有]文件进行差异比较，并恢复所有受影响文件的上下文：

`fixfiles -C PREVIOUS_FILECONTEXT`

- 只对在特定日期之后创建的文件进行操作，该日期将传递给find的`--newermt`命令：

`fixfiles -N {{YYYY-MM-DD HH:MM}}`

- 在重新标记文件系统之前绑定[M]ount文件系统，这允许修复已被挂载的文件或目录的上下文：

`fixfiles -M`

- 将[v]erbosity从进度修改为详细，并使用`-v`而不是`-p`运行`restorecon`：

`fixfiles -v`