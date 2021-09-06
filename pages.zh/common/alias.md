# alias

> 创建别名 -- 用给定的字符串指代特定的命令。
> 别名只会在当前的 shell 会话中生效，除非它们在 shell 的配置文件中被定义，例如`~/.bashrc`.
> 更多信息：<https://tldp.org/LDP/abs/html/aliases.html>.

- 创建一个通用的别名：

`alias {{别名}}="{{命令}}"`

- 通过给定的别名查看它所指代的命令：

`alias {{别名}}`

- 移除一个别名：

`unalias {{别名}}`

- 列出所有的别名：

`alias -p`

- 将 rm 转换为交互式命令：

`alias {{rm}}="{{rm -i}}"`

- 创建别名`la`来指代`ls -a`:

`alias {{la}}="{{ls -a}}"`
