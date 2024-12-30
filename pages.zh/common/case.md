# case

> Bash 内置结构，用于创建多选条件语句。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-case>。

- 将变量与字符串字面量进行匹配，以决定运行哪个命令：

`case {{$tocount}} in {{words}}) {{wc -w README}}; ;; {{lines}}) {{wc -l README}}; ;; esac`

- 使用 | 组合模式，使用 * 作为后备模式：

`case {{$tocount}} in {{[wW]|words}}) {{wc -w README}}; ;; {{[lL]|lines}}) {{wc -l README}}; ;; *) {{echo "what?"}}; ;; esac`