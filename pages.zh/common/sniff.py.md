# sniff.py

> 使用 pcapy 库捕获和显示网络数据包。
> 是 Impacket 套件的一部分。
> 更多信息：<https://github.com/fortra/impacket>.

- 列出可用的网络接口并选择一个开始捕获数据包（需要 `sudo`）：

`sudo sniff.py`

- 捕获数据包并将其输出保存到文件中，同时在终端显示：

`sudo sniff.py | sudo tee {{output_file}}`
