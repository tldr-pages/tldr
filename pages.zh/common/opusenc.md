# opusenc

> 将WAV或FLAC音频转换为Opus格式。
> 更多信息请访问：<https://opus-codec.org/docs/opus-tools/opusenc.html>。

- 使用默认选项将WAV转换为Opus：

`opusenc {{path/to/input.wav}} {{path/to/output.opus}}`

- 以最高质量水平转换立体声音频：

`opusenc --bitrate {{512}} {{path/to/input.wav}} {{path/to/output.opus}}`

- 以最高质量水平转换5.1环绕声音频：

`opusenc --bitrate {{1536}} {{path/to/input.flac}} {{path/to/output.opus}}`

- 以最低质量水平转换语音音频：

`opusenc {{path/to/input.wav}} --downmix-mono --bitrate {{6}} {{path/to/out.opus}}`