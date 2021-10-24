# at

> 在指定时间执行命令。
> 更多信息：<https://man.archlinux.org/man/at.1>.

- 打开 `at` 提示符创建一组新的定时命令，按 `Ctrl + D` 保存并退出：

`at {{hh:mm}}`

- 运行命令并通过本地电子邮件程序（例如 sendmail）发送运行结果：

`at {{hh:mm}} -m`

- 在指定时间执行一个脚本：

`at {{hh:mm}} -f {{文件路径}}`

- 在二月十八号下午十一点发送系统通知：

`echo "notify-send '{{Wake up!}}'" | at {{11pm}} {{Feb 18}}`
