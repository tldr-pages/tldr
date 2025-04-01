# stegsnow

> 用于在文本文件中隐藏和提取消息的工具，消息以制表符和空格编码。
> 更多信息：<https://darkside.com.au/snow/manual.html>.

- 从文件中提取消息:

`stegsnow {{path/to/file.txt}}`

- 从文件中提取压缩并密码保护的消息:

`stegsnow -C -p {{password}} {{path/to/file.txt}}`

- 确定文件的近似存储容量，行长度小于72：

`stegsnow -S -l 72 {{path/to/file.txt}}`

- 将消息隐藏在文本中并保存到结果文件:

`stegsnow -m '{{message}}' {{path/to/file.txt}} {{path/to/result.txt}}`

- 将消息文件内容压缩并隐藏在文本中，保存到结果文件:

`stegsnow -C -f '{{path/to/message.txt}}' {{path/to/file.txt}} {{path/to/result.txt}}`

- 将消息压缩并密码保护后隐藏在文本中，保存到结果文件:

`stegsnow -C -p {{password}} -m '{{message}}' {{path/to/file.txt}} {{path/to/result.txt}}`
