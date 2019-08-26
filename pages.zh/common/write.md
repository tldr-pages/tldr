# write

> 向某个终端上的特定用户的屏幕写入信息 (ctrl-C 来停止写入).
> 使用 `who` 命令来获取所有活动用户的终端id. 参见 `mesg`.

- 向指定的终端ID上的指定用户写入信息:

`write {{username}} {{terminal_id}}`

- 向终端 "/dev/tty/5" 上的用户 "testuser" 发送信息:

`write {{testuser}} {{tty/5}}`

- 向伪终端 "/dev/pts/5" 上的用户 "jhondoe" 发送信息 :

`write {{jhondoe}} {{pts/5}}`
