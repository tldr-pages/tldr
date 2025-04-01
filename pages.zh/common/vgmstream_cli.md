# vgmstream_cli

> 播放各种视频游戏中使用的音频格式，并将其转换为 `wav`。
> 更多信息：<https://github.com/vgmstream/vgmstream/blob/master/doc/USAGE.md>。

- 将 `adc` 文件解码为 `wav`。（默认输出名称为 `input.wav`）：

`vgmstream_cli {{path/to/input.adc}} -o {{path/to/output.wav}}`

- 打印元数据而不解码音频：

`vgmstream_cli {{path/to/input.adc}} -m`

- 不含循环地解码音频文件：

`vgmstream_cli {{path/to/input.adc}} -o {{path/to/output.wav}} -i`

- 解码音频文件并设置三次循环，然后添加 3 秒延迟，再进行 5 秒淡出：

`vgmstream_cli {{path/to/input.adc}} -o {{path/to/output.wav}} -l {{3.0}} -f {{5.0}} -d {{3.0}}`

- 将多个文件转换为 `bgm_(原始名称).wav`（默认 `-o` 模式为 `?f.wav`）：

`vgmstream_cli -o {{path/to/bgm_?f.wav}} {{path/to/file1.adc}} {{path/to/file2.adc}}`

- 循环播放文件（`channels` 和 `rate` 必须与元数据匹配）：

`vgmstream_cli {{path/to/input.adc}} -pec | aplay --format cd --channels {{1}} --rate {{44100}}`