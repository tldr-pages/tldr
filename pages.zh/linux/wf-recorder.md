# wf-recorder

> 用于 Wayland 的屏幕录制工具，可选包含音频。
> 默认情况下，需要使用 `<Ctrl+c>` 结束录制过程。
> 更多信息：<https://github.com/ammen99/wf-recorder>。

- 录制并保存为 MP4 文件：

`wf-recorder --file={{output.mp4}}`

- 录制包括音频，同时包含麦克风和系统声音：

`wf-recorder --audio --file={{/path/to/file_with_audio.webm}}`

- 使用 `slurp` 选择并录制屏幕的一部分，输出到默认的 `recording.mp4`：

`wf-recorder -g "$(slurp)"`