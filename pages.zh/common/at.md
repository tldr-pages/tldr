# at

> 在一段时间后，执行单次命令。
> atd 服务（或 atrun）需要处于运行状态，以保证命令成功执行。
> 更多信息：<https://man.archlinux.org/man/at.1>.

- 5 分钟后，执行标准输入中的命令（命令输入完成后按 `Ctrl + D`）：

`at now + {{5 minutes}}`

- 在今天上午 10:00 执行标准输入中的命令：

`echo "{{./make_db_backup.sh}}" | at {{1000}}`

- 下周二晚上 9:30 执行指定文件中包含的命令：

`at -f {{path/to/file}} {{9:30 PM Tue}}`
