# bash

> Bourne-Again SHell.
> 兼容`sh`的命令行解释器。
> 更多信息：<https://www.gnu.org/software/bash/>.

- 启动交互式 shell：

`bash`

- 执行命令：

`bash -c "{{command}}"`

- 执行脚本文件：

`bash {{file.sh}}`

- 执行脚本文件，并将所有执行过的命令输出到终端：

`bash -x {{file.sh}}`

- 执行脚本文件，并在第一个错误处终止：

`bash -e {{file.sh}}`
