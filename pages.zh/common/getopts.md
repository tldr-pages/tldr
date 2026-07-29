# getopts

> 从参数中解析 shell 选项。
> 注意：此命令不支持长格式选项，因此建议使用 `getopt`。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-getopts>。

- 检查选项是否是当前上下文中第一个设置的选项：

`getopts {{x}} {{opt}}; echo ${{opt}}`

- 检查字符串中是否设置了选项（指定的选项必须是字符串的第一个元素）：

`getopts {{x}} {{opt}} "{{文本字符串}}"; echo ${{opt}}`

- 设置选项需要参数并打印它们：

`getopts {{x}}: {{opt}}; echo ${{opt}} $OPTARG`

- 检查多个选项：

`while getopts {{xyz}} {{opt}}; do case ${{opt}} in x) {{echo x 已设置}};; y) {{echo y 已设置}};; z) {{echo z 已设置}};; esac; done`

- 将 `getopts` 设置为静默模式并处理选项错误：

`while getopts :{{x:}} {{opt}}; do case ${{opt}} in x) ;; :) {{echo "需要参数"}};; ?) {{echo "无效参数"}} esac;; done`

- 重置 `getopts`：

`OPTIND=1`
