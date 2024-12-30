# stegsnow

> 隐写工具，用于在编码为制表符和空格的文本文件中隐藏和提取消息。
> 更多信息请访问: <https://darkside.com.au/snow/manual.html>.

- 从文件中提取 [m]消息：

`stegsnow {{path/to/file.txt}}`

- 从文件中提取 [C]压缩和 [p]密码保护的 [m]消息：

`stegsnow -C -p {{password}} {{path/to/file.txt}}`

- 确定文件的近似 [S]存储容量，行 [l]长度小于 72：

`stegsnow -S -l 72 {{path/to/file.txt}}`

- 在文件的文本中隐藏 [m]消息并保存到结果中：

`stegsnow -m '{{message}}' {{path/to/file.txt}} {{path/to/result.txt}}`

- 在文件的文本中隐藏消息 [f]文件内容 [C]压缩并保存到结果中：

`stegsnow -C -f '{{path/to/message.txt}}' {{path/to/file.txt}} {{path/to/result.txt}}`

- 在文件的文本中隐藏 [m]消息 [C]压缩和 [p]密码保护并保存到结果中：

`stegsnow -C -p {{password}} -m '{{message}}' {{path/to/file.txt}} {{path/to/result.txt}}`