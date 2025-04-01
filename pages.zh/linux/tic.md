# tic

> 编译 terminfo 并为 ncurses 安装。
> 更多信息：<https://pubs.opengroup.org/onlinepubs/007908799/xcurses/terminfo.html>.

- 编译并安装指定终端的 terminfo：

`tic -xe {{terminal}} {{path/to/terminal.info}}`

- 检查 terminfo 文件是否有错误：

`tic -c {{path/to/terminal.info}}`

- 打印数据库位置：

`tic -D`