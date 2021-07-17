# echo

> 输出给定参数。
> 更多信息：<https://www.gnu.org/software/coreutils/echo>.

- 输出文本信息. 注意： 引号是可选的：

`echo "{{Hello World}}"`

- 输出带有环境变量的信息：

`echo "{{My path is $PATH}}"`

- 打印不带尾随换行符的信息：

`echo -n "{{Hello World}}"`

- 向文件添加信息：

`echo "{{Hello World}}" >> {{file.txt}}`

- 启用反斜杠转义的解释（特殊字符）：

`echo -e "{{Column 1\tColumn 2}}"`
