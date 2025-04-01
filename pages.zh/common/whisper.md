# whisper

> 将音频文件转换为 `txt`、`vtt`、`srt`、`tsv` 和 `json` 格式。
> 更多信息：<https://github.com/openai/whisper>.

- 将特定的音频文件转换为指定的所有文件格式：

`whisper {{path/to/audio.mp3}}`

- 转换音频文件并指定转换后文件的输出格式：

`whisper {{path/to/audio.mp3}} --output_format {{txt}}`

- 使用特定模型转换音频文件：

`whisper {{path/to/audio.mp3}} --model {{tiny.en,tiny,base.en,base,small.en,small,medium.en,medium,large-v1,large-v2,large}}`

- 指定音频文件的语言以减少转换时间：

`whisper {{path/to/audio.mp3}} --language {{english}}`

- 转换音频文件并保存到特定位置：

`whisper {{path/to/audio.mp3}} --output_dir "{{path/to/output}}"`

- 以静默模式转换音频文件：

`whisper {{path/to/audio.mp3}} --verbose {{False}}`
