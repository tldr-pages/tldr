# powertop

> 优化电池电力使用。
> 更多信息：<https://github.com/fenrus75/powertop>。

- 校准电力使用测量：

`sudo powertop --calibrate`

- 在当前目录生成 HTML 电力使用报告：

`sudo powertop --html={{power_report.html}}`

- 调整至最佳设置：

`sudo powertop --auto-tune`

- 生成指定秒数的报告（默认是 20 秒）：

`sudo powertop --time={{5}}`