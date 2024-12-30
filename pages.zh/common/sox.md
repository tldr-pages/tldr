# sox

> 声音交换：播放、录制和转换音频文件。
> 音频格式由扩展名识别。
> 更多信息：<https://sox.sourceforge.net>。

- 将两个音频文件合并为一个：

`sox -m {{path/to/input_audio1}} {{path/to/input_audio2}} {{path/to/output_audio}}`

- 将音频文件修剪到指定时间：

`sox {{path/to/input_audio}} {{path/to/output_audio}} trim {{start}} {{duration}}`

- 标准化音频文件（调整音量至最大峰值水平，而不失真）：

`sox --norm {{path/to/input_audio}} {{path/to/output_audio}}`

- 反转并保存音频文件：

`sox {{path/to/input_audio}} {{path/to/output_audio}} reverse`

- 打印音频文件的统计数据：

`sox {{path/to/input_audio}} -n stat`

- 将音频文件的音量提高2倍：

`sox -v 2.0 {{path/to/input_audio}} {{path/to/output_audio}}`