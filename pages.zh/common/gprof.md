# gprof

> 多种编程语言的性能分析工具。
> 它对程序的函数执行进行分析。
> 更多信息请访问：<https://ftp.gnu.org/old-gnu/Manuals/gprof-2.9.1/html_mono/gprof.html>。

- 使用 gprof 信息编译二进制文件并运行以获取 `gmon.out`：

`gcc -pg {{program.c}} && {{./a.out}}`

- 运行 gprof 获取分析输出：

`gprof`

- 抑制分析字段的描述：

`gprof -b`

- 显示使用次数为零的例程：

`gprof -bz`