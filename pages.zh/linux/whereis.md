# whereis

> 查找命令的二进制文件、源文件和手册页文件。
> 更多信息：<https://manned.org/whereis>.

- 查找 SSH 的二进制文件、源文件和手册页：

`whereis {{ssh}}`

- 查找 ls 的 [b]二进制文件和 [m]手册页：

`whereis -bm {{ls}}`

- 查找 gcc 的 [s]源文件和 Git 的 [m]手册页：

`whereis -s {{gcc}} -m {{git}}`

- 只在 `/usr/bin/` 目录中查找 gcc 的 [b]二进制文件：

`whereis -b -B {{/usr/bin/}} -f {{gcc}}`

- 查找系统中数量异常的 [u]二进制文件（数量多于或少于一个的二进制文件）：

`whereis -u *`

- 查找具有 [u]异常 [m]手册条目的二进制文件（安装的手册页数量多于或少于一个的二进制文件）：

`whereis -u -m *`