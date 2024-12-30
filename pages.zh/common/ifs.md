# IFS

> IFS（内部字段分隔符）是一个特殊的环境变量，用于定义在Unix shell中进行单词拆分时使用的分隔符。
> IFS的默认值是空格、制表符和换行符。这三个字符作为分隔符使用。
> 更多信息：<https://www.gnu.org/software/bash/manual/html_node/Word-Splitting.html>。

- 查看当前的IFS值：

`echo "$IFS"`

- 修改IFS值：

`IFS="{{:}}"`

- 将IFS重置为默认值：

`IFS=$' \t\n'`

- 在子shell中临时改变IFS值：

`(IFS="{{:}}"; echo "{{one:two:three}}")`