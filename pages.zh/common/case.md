# case

> case ... esac 与其他语言中的 switch ... case 语句类似，是一种多分枝选择结构。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-case>.

- 通过字符串字面量判断执行分支：

`case {{入参变量}} in {{字符字面量}}) {{wc -w 执行语句块}}; ;; {{字符串}}) {{wc -l 执行语句块}}; ;; esac`

- 搭配通配符进行匹配，判断执行分支：

`case {{入参变量}} in {{[wW]|字符字面量}}) {{wc -w 执行语句块}}; ;; {{[lL]|字符串}}) {{执行语句块}}; ;; *) {{echo "what?"}}; ;; esac`
