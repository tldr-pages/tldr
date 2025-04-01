# gnuplot

> 一个能够输出多种格式的图表绘制工具。
> 更多信息：<http://www.gnuplot.info/>.

- 启动交互式的图表绘制 shell：

`gnuplot`

- 为指定的图表定义文件绘制图表：

`gnuplot {{path/to/definition.plt}}`

- 在加载定义文件之前执行命令以设置输出格式：

`gnuplot -e "{{set output "path/to/filename.png" size 1024,768}}" {{path/to/definition.plt}}`

- gnuplot 退出后保持图表预览窗口打开：

`gnuplot {{[-p|--persist]}} {{path/to/definition.plt}}`