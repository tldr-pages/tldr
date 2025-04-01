# pulseaudio

> PulseAudio 声音系统守护进程和管理器。
> 更多信息：<https://www.freedesktop.org/wiki/Software/PulseAudio/>。

- 检查 PulseAudio 是否正在运行（非零退出代码表示未运行）：

`pulseaudio --check`

- 在后台启动 PulseAudio 守护进程：

`pulseaudio --start`

- 终止正在运行的 PulseAudio 守护进程：

`pulseaudio --kill`

- 列出可用模块：

`pulseaudio --dump-modules`

- 将指定参数的模块加载到正在运行的守护进程中：

`pulseaudio --load="{{module_name}} {{arguments}}"`