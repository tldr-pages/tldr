# dmd

> 官方 D 编译器。
> 更多信息：<https://dlang.org/dmd.html>。

- 编译 D 源文件：

`dmd {{path/to/source.d}}`

- 为所有模板实例生成代码：

`dmd -allinst`

- 控制边界检查：

`dmd -boundscheck={{on|safeonly|off}}`

- 列出所有可用检查的信息：

`dmd -check={{h|help|?}}`

- 开启彩色控制台输出：

`dmd -color`