# wf-recorder

> Wayland的屏幕录制工具，可选带音频。
> 默认情况下，您需要使用Ctrl-C结束进程。
> 更多信息：<https://github.com/ammen99/wf-recorder>。

- 将录制保存为MP4文件：

`wf-recorder --file={{output.mp4}}`

- 录制包括音频，既有麦克风声音也有系统声音：

`wf-recorder --audio --file={{/path/to/file_with_audio.webm}}`

- 使用`slurp`选择并录制屏幕的一部分，输出到默认的`recording.mp4`：

`wf-recorder -g "$(slurp)"`