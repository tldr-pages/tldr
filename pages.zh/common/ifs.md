# IFS

> IFS（内部字段分隔符）是一个特殊的环境变量，用于定义 Unix shell 中单词分割时使用的分隔符。
> IFS 的默认值为空格、制表符和换行符。这三个字符作为分隔符使用。
> 更多信息：<https://www.gnu.org/software/bash/manual/html_node/Word-Splitting.html>.

- 查看当前的 IFS 值：

`echo "$IFS"`

- 更改 IFS 值：

`IFS="{{:}}"`

- 重置 IFS 为默认值：

`IFS=$' \t\n'`

- 在子 shell 中临时更改 IFS 值：

`(IFS="{{:}}"; echo "{{one:two:three}}")`