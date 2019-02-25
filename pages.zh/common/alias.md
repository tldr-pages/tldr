# alias

> 创建别名 -- 用给定的字符串指代特定的命令.
> 别名只会在当前的shell会话中生效, 除非它们在shell的配置文件中被定义, 例如`~/.bashrc`.

- 创建一个通用的别名:

`alias {{word}}="{{command}}"`

- 通过给定的别名查看它所指代的命令:

`alias {{word}}`

- 移除一个别名:

`unalias {{word}}`

- 列出所有的别名:

`alias -p`

- 将rm转换为交互式命令:

`alias {{rm}}="{{rm -i}}"`

- 创建别名`la`来指代`ls -a`:

`alias {{la}}="{{ls -a}}"`
