# steghide

> 针对JPEG、BMP、WAV和AU文件格式的隐写工具。
> 更多信息：<https://github.com/StefanoDeVuono/steghide>。

- 在PNG中嵌入数据，提示输入密码短语：

`steghide embed --coverfile {{path/to/image.png}} --embedfile {{path/to/data.txt}}`

- 从WAV音频文件中提取数据：

`steghide extract --stegofile {{path/to/sound.wav}}`

- 显示文件信息，尝试检测嵌入的文件：

`steghide info {{path/to/file.jpg}}`

- 在JPEG图像中嵌入数据，使用最大压缩：

`steghide embed --coverfile {{path/to/image.jpg}} --embedfile {{path/to/data.txt}} --compress {{9}}`

- 获取支持的加密算法和模式列表：

`steghide encinfo`

- 在JPEG图像中嵌入加密数据，例如使用CBC模式的Blowfish：

`steghide embed --coverfile {{path/to/image.jpg}} --embedfile {{path/to/data.txt}} --encryption {{blowfish|...}} {{cbc|...}}`