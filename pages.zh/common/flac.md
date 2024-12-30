# flac

> 编码、解码和测试FLAC文件。
> 更多信息：<https://xiph.org/flac>。

- 将WAV文件编码为FLAC（这将创建一个与WAV文件位于同一位置的FLAC文件）：

`flac {{path/to/file.wav}}`

- 将WAV文件编码为FLAC，指定输出文件：

`flac -o {{path/to/output.flac}} {{path/to/file.wav}}`

- 将FLAC文件解码为WAV，指定输出文件：

`flac -d -o {{path/to/output.wav}} {{path/to/file.flac}}`

- 测试FLAC文件的正确编码：

`flac -t {{path/to/file.flac}}`