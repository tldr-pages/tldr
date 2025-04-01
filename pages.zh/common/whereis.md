# whereis

> 找到命令的二进制文件、源文件和手册文件。
> 更多信息：<https://manned.org/whereis>.

- 找到 SSH 命令的二进制、源文件和手册页：

`whereis {{ssh}}`

- 查找 `ls` 命令的二进制和手册页：

`whereis -bm {{ls}}`

- 找到 `gcc` 的源文件和 `git` 的手册页：

`whereis -s {{gcc}} -m {{git}}`

- 仅在 /usr/bin/ 目录中查找 `gcc` 的二进制文件：

`whereis -b -B {{/usr/bin/}} -f {{gcc}}`

- 查找不寻常的二进制文件（系统上有多个或少于一个二进制文件的二进制文件）：

`whereis -u *`

- 查找有不寻常手册条目的二进制文件（安装了多个或少于一个手册的二进制文件）：

`whereis -u -m *`
