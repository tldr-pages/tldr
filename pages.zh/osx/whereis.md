# whereis

> 找到命令的二进制,源文件和手册文件.

- 找到 `ssh` 命令的二进制、源文件和手册页:

`whereis {{ssh}}`

- 查找 `ls` 命令的二进制和手册页:

`whereis -bm {{ls}}`

- 找到 `gc` 的源文件和 `git` 的手册页:

`whereis -s {{gcc}} -m {{git}}`

- 仅在 /usr/bin/ 目录中查找 `gcc` 的二进制文件:

`whereis -b -B {{/usr/bin/}} -f {{gcc}}`
