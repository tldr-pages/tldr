# case

> Bash 内置的多重条件语句结构。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-case>.

- 通过字符串字面量判断执行分支：

`case {{$计数规则}} in {{字数}}) {{wc -w README}} ;; {{行数}}) {{wc -l README}} ;; esac`

- 使用 | 组合匹配模式，使用 * 作为默认匹配：

`case {{$计数规则}} in {{[wW]|字数}}) {{wc -w README}} ;; {{[lL]|行数}}) {{wc -l README}} ;; *) {{echo "无效输入"}} ;; esac`

- 允许匹配多个模式：

`case {{$动物}} in {{猫}}) echo "这是一只猫" ;;& {{猫|狗}}) echo "这是一只猫或狗" ;;& *) echo "其他动物" ;; esac`

- 继续执行下一个模式的命令而不检查模式：

`case {{$动物}} in {{猫}}) echo "这是一只猫" ;& {{狗}}) echo "这是一只狗或猫的匹配结果" ;& *) echo "其他动物" ;; esac`

- 显示帮助：

`help case`
