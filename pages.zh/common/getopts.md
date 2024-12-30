# getopts

> 从参数中解析 shell 选项。
> 该命令不支持长格式选项，因此建议使用 `getopt`。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-getopts>。

- 检查选项是否设置：

`getopts {{x}} {{opt}}; echo $opt`

- 设置选项以要求参数并检查该参数：

`getopts {{x}}: {{opt}}; echo $OPTARG`

- 检查多个选项：

`while getopts {{xyz}} {{opt}}; do case $opt in x) echo x is set;; y) echo y is set;; z) echo z is set;; esac; done`

- 将 `getopts` 设置为静默模式并处理选项错误：

`while getopts :{{x:}} {{opt}}; do case $opt in x) ;; :) echo "需要参数";; ?) echo "无效参数" esac;; done`

- 重置 `getopts`：

`OPTIND=1`