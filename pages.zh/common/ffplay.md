# ffplay

> 一个简单且便携的媒体播放器，使用 FFmpeg 库和 SDL 库。
> 更多信息：<https://ffmpeg.org/ffplay-all.html>。

- 播放媒体文件：

`ffplay {{path/to/file}}`

- 无 GUI 播放媒体文件中的音频：

`ffplay -nodisp {{path/to/file}}`

- 通过 `stdin` 播放由 `ffmpeg` 传递的媒体：

`ffmpeg -i {{path/to/file}} -c {{copy}} -f {{media_format}} - | ffplay -`

- 播放视频并实时显示运动矢量：

`ffplay -flags2 +export_mvs -vf codecview=mv=pf+bf+bb {{path/to/file}}`

- 仅显示视频关键帧：

`ffplay -vf select="{{eq(pict_type\,PICT_TYPE_I)}}" {{path/to/file}}`