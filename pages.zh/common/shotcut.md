# shotcut

> 一款视频编辑程序。
> 更多信息：<https://shotcut.org/notes/command-line-options/>。

- 启动Shotcut：

`shotcut`

- 打开音频/视频文件：

`shotcut {{path/to/file1 path/to/file2 ...}}`

- 使用特定音频驱动程序启动：

`shotcut --SDL_AUDIODRIVER "{{pulseaudio}}"`

- 以全屏模式启动：

`shotcut --fullscreen`

- 启动时使用GPU处理：

`shotcut --gpu`