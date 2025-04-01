# sox

> Sound eXchange: 播放、录制和转换音频文件。
> 音频格式通过扩展名识别。
> 更多信息：<https://sox.sourceforge.net>。

- 将两个音频文件合并为一个：

`sox -m {{path/to/input_audio1}} {{path/to/input_audio2}} {{path/to/output_audio}}`

- 将音频文件裁剪到指定时间：

`sox {{path/to/input_audio}} {{path/to/output_audio}} trim {{start}} {{duration}}`

- 归一化音频文件（调整音量到最大峰值水平，不剪辑）：

`sox --norm {{path/to/input_audio}} {{path/to/output_audio}}`

- 反转并保存音频文件：

`sox {{path/to/input_audio}} {{path/to/output_audio}} reverse`

- 打印音频文件的统计信息：

`sox {{path/to/input_audio}} -n stat`

- 将音频文件的音量增加2倍：

`sox -v 2.0 {{path/to/input_audio}} {{path/to/output_audio}}`