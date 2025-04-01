# opusenc

> 将 WAV 或 FLAC 音频转换为 Opus。
> 更多信息：<https://opus-codec.org/docs/opus-tools/opusenc.html>.

- 使用默认选项将 WAV 转换为 Opus：

`opusenc {{path/to/input.wav}} {{path/to/output.opus}}`

- 以最高质量级别转换立体声音频：

`opusenc --bitrate {{512}} {{path/to/input.wav}} {{path/to/output.opus}}`

- 以最高质量级别转换 5.1 环绕声音频：

`opusenc --bitrate {{1536}} {{path/to/input.flac}} {{path/to/output.opus}}`

- 以最低质量级别转换语音音频：

`opusenc {{path/to/input.wav}} --downmix-mono --bitrate {{6}} {{path/to/out.opus}}`
