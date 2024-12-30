# gnuplot

> 一个可以以多种格式输出图形的绘图工具。
> 更多信息：<http://www.gnuplot.info/>。

- 启动交互式绘图命令行：

`gnuplot`

- 根据指定的图形定义文件绘制图形：

`gnuplot {{path/to/definition.plt}}`

- 在加载定义文件之前通过执行命令设置输出格式：

`gnuplot -e "{{set output "path/to/filename.png" size 1024,768}}" {{path/to/definition.plt}}`

- 在gnuplot退出后保持图形绘制预览窗口：

`gnuplot --persist {{path/to/definition.plt}}`