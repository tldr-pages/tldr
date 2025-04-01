# xwinwrap

> 将一个播放器或程序作为桌面背景运行。
> 更多信息：<https://github.com/ujjwal96/xwinwrap>。

- 使用 mpv 播放视频：

`xwinwrap -b -nf -ov -- {{mpv}} -wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{path/to/video.mp4}}`

- 使用 mpv 全屏播放视频：

`xwinwrap -b -nf -fs -ov -- {{mpv}} -wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{path/to/video.mp4}}`

- 使用 mpv 播放视频并设置 80% 透明度：

`xwinwrap -b -nf -ov -o 0.8 --- {{mpv}} -wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{path/to/video.mp4}}`

- 在第二显示器（分辨率为 1600x900，X 轴偏移 1920）上使用 mpv 播放视频：

`xwinwrap -g 1600x900+1920 -b -nf -ov -- {{mpv}} -wid {{wid}} --loop --no-audio --no-resume-playback --panscan={{1.0}} {{path/to/video.mkv}}`