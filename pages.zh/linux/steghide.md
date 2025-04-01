# steghide

> 针对 JPEG、BMP、WAV 和 AU 文件格式的隐写工具。
> 更多信息：<https://github.com/StefanoDeVuono/steghide>.

- 将数据嵌入 PNG 图像，并提示输入密码：

`steghide embed --coverfile {{path/to/image.png}} --embedfile {{path/to/data.txt}}`

- 从 WAV 音频文件中提取数据：

`steghide extract --stegofile {{path/to/sound.wav}}`

- 显示文件信息，尝试检测嵌入的文件：

`steghide info {{path/to/file.jpg}}`

- 将数据嵌入 JPEG 图像，并使用最大压缩：

`steghide embed --coverfile {{path/to/image.jpg}} --embedfile {{path/to/data.txt}} --compress {{9}}`

- 获取支持的加密算法和模式列表：

`steghide encinfo`

- 将加密数据嵌入 JPEG 图像，例如使用 Blowfish 算法的 CBC 模式：

`steghide embed --coverfile {{path/to/image.jpg}} --embedfile {{path/to/data.txt}} --encryption {{blowfish|...}} {{cbc|...}}`