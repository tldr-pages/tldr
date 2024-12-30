# whereis

> 定位命令的二进制文件、源代码和手册页文件。
> 更多信息：<https://manned.org/whereis>。

- 定位 SSH 的二进制文件、源代码和手册页：

`whereis {{ssh}}`

- 定位 ls 的二进制文件和手册页：

`whereis -bm {{ls}}`

- 定位 gcc 的源代码和 Git 的手册页：

`whereis -s {{gcc}} -m {{git}}`

- 仅在 `/usr/bin/` 中定位 gcc 的二进制文件：

`whereis -b -B {{/usr/bin/}} -f {{gcc}}`

- 定位不寻常的二进制文件（在系统上具有多于或少于一个的二进制文件）：

`whereis -u *`

- 定位具有不寻常手册条目的二进制文件（安装的手册少于或多于一个的二进制文件）：

`whereis -u -m *`