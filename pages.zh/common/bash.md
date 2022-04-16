# bash

> Bourne-Again SHell.
> 兼容`sh`的命令行解释器。
> 更多信息：<https://gnu.org/software/bash/>.

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

- 从输入（stdin）读取命令：

`bash -s`

- 将跟随的所有选项原样传递到要执行的脚本文件（可与`-s`选项共用来将选项传递到来自输入的命令 / 脚本）：

`bash --`

- 打印 bash 的版本信息（使用`echo $BASH_VERSION`来获得纯粹的版本字符串）：

`bash --version`
