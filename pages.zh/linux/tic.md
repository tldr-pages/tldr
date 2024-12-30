# tic

> 编译终端信息并为 ncurses 安装。
> 更多信息：<https://pubs.opengroup.org/onlinepubs/007908799/xcurses/terminfo.html>。

- 为终端编译并安装终端信息：

`tic -xe {{terminal}} {{path/to/terminal.info}}`

- 检查终端信息文件的错误：

`tic -c {{path/to/terminal.info}}`

- 打印数据库位置：

`tic -D`