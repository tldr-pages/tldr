# tesseract

> OCR（光学字符识别）引擎。
> 更多信息：<https://github.com/tesseract-ocr/tesseract>。

- 识别图像中的文本并保存到 `output.txt`（`.txt` 扩展名会自动添加）：

`tesseract {{image.png}} {{output}}`

- 使用 ISO 639-2 代码指定自定义语言（默认语言为英语），例如 deu = Deutsch = 德语：

`tesseract -l deu {{image.png}} {{output}}`

- 列出可用语言的 ISO 639-2 代码：

`tesseract --list-langs`

- 指定自定义页面分割模式（默认模式为 3）：

`tesseract --psm {{0_to_10}} {{image.png}} {{output}}`

- 列出页面分割模式及其描述：

`tesseract --help-psm`