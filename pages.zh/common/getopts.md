# getopts

> 解析命令行参数中的 shell 选项。
> 该命令不支持长选项，因此建议使用 `getopt`。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-getopts>。

- 检查某个选项是否已设置：

`getopts {{x}} {{opt}}; echo $opt`

- 设置一个选项要求参数，并检查该参数：

`getopts {{x}}: {{opt}}; echo $OPTARG`

- 检查多个选项：

`while getopts {{xyz}} {{opt}}; do case $opt in x) echo x 已设置;; y) echo y 已设置;; z) echo z 已设置;; esac; done`

- 将 `getopts` 设置为静默模式并处理选项错误：

`while getopts :{{x:}} {{opt}}; do case $opt in x) ;; :) echo "缺少参数";; ?) echo "无效的参数" esac;; done`

- 重置 `getopts`：

`OPTIND=1`