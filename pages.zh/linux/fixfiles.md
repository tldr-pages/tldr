# fixfiles

> 修复文件的 SELinux 安全上下文。
> 更多信息：<https://manned.org/fixfiles>.

- 如果与 onboot 一起使用，此 fixfiles 会在 `/.autorelabel` 文件中记录当前日期，以便稍后可以加快标签处理。如果与 restore 一起使用，则仅会影响今天修改的文件：

`fixfiles -B`

- [F]orce 重置上下文以匹配 `file_context`，适用于可自定义的文件：

`fixfiles -F`

- 不需要确认直接清除 `/tmp` 目录：

`fixfiles -f`

- 使用 [R]pm 数据库发现特定软件包中的所有文件并恢复文件上下文：

`fixfiles -R {{rpm_package1,rpm_package2 ...}}`

- 对 `PREVIOUS_FILECONTEXT` 文件与 [C]urrently 安装的文件进行差异比较，并恢复所有受影响文件的上下文：

`fixfiles -C PREVIOUS_FILECONTEXT`

- 仅作用于特定日期后创建的文件，这些日期将传递给 find `--newermt` 命令：

`fixfiles -N {{YYYY-MM-DD HH:MM}}`

- 在重新标记之前绑定 [M]ount 文件系统，这允许修复已挂载覆盖的文件或目录的上下文：

`fixfiles -M`

- 将 [v]erbosity 从进度更改为详细，并用 `-v` 代替 `-p` 运行 `restorecon`：

`fixfiles -v`