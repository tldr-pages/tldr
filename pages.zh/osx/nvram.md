# nvram

> 操作固件变量。
> 更多信息：<https://keith.github.io/xcode-man-pages/nvram.8.html>。

- [p] 打印存储在 NVRAM 中的所有变量：

`nvram -p`

- [p] 以 [x]ML 格式打印存储在 NVRAM 中的所有变量：

`nvram -xp`

- 修改固件变量的值：

`sudo nvram {{name}}="{{value}}"`

- [d] 删除一个固件变量：

`sudo nvram -d {{name}}`

- [c] 清除所有固件变量：

`sudo nvram -c`

- 从特定的 [x]ML [f] 文件设置一个固件变量：

`sudo nvram -xf {{path/to/file.xml}}`