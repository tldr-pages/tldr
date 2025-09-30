# base64

> 使用 Base64 来进行编码和解码。
> 更多信息：<https://keith.github.io/xcode-man-pages/bintrans.1>.

- 编码目标文件：

`base64 {{[-i|--input]}} {{目标文件}}`

- 解码目标文件：

`base64 {{[-d|--decode]}} {{[-i|--input]}} {{base64 编码文件}}`

- 通过标准输入管道进行解码：

`echo -n "{{目标字符串}}" | base64`

- 解码标准输入管道内容：

`echo -n {{base64 字符串}} | base64 {{[-d|--decode]}}`
