# gprof

> 用于多种编程语言的性能分析工具。
> 它分析程序的函数执行情况。
> 更多信息：<https://ftp.gnu.org/old-gnu/Manuals/gprof-2.9.1/html_mono/gprof.html>.

- 将二进制文件编译为默认的 `a.out`，并包含 gprof 信息，然后运行它以生成 `gmon.out`：

`gcc {{[-p|-pg]}} {{program.c}} && ./a.out`

- 对默认的 `a.out` 和 `gmon.out` 运行 gprof 以获得分析输出：

`gprof`

- 对指定的二进制文件运行 gprof：

`gprof {{path/to/binary}} {{path/to/gmon.out}}`

- 抑制显示分析字段的描述：

`gprof {{[-b|--brief]}}`

- 显示使用率为零的例程：

`gprof {{[-bz|--brief --display-unused-functions]}}`