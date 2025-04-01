# gimp

> GNU 图像处理程序。
> 另见: `krita`。
> 更多信息: <https://docs.gimp.org/en/gimp-fire-up.html#gimp-concepts-running-command-line>。

- 启动 GIMP：

`gimp`

- 打开特定文件：

`gimp {{path/to/image1 path/to/image2 ...}}`

- 在新窗口中打开特定文件：

`gimp --new-instance {{path/to/image1 path/to/image2 ...}}`

- 不显示启动画面启动 GIMP：

`gimp --no-splash`

- 将错误和警告打印到控制台，而不是在对话框中显示：

`gimp --console-messages`

- 启用调试信号处理器：

`gimp --debug-handlers`
