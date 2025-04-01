# flac

> 编码、解码和测试 FLAC 文件。
> 更多信息：<https://xiph.org/flac>.

- 将 WAV 文件编码为 FLAC（这将在 WAV 文件所在的同一位置创建一个 FLAC 文件）：

`flac {{path/to/file.wav}}`

- 将 WAV 文件编码为 FLAC，并指定输出文件：

`flac -o {{path/to/output.flac}} {{path/to/file.wav}}`

- 将 FLAC 文件解码为 WAV，并指定输出文件：

`flac -d -o {{path/to/output.wav}} {{path/to/file.flac}}`

- 测试 FLAC 文件的编码是否正确：

`flac -t {{path/to/file.flac}}`