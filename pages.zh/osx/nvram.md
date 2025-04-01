# nvram

> 操作固件变量。
> 更多信息：<https://keith.github.io/xcode-man-pages/nvram.8.html>.

- [p]rint 打印存储在 NVRAM 中的所有变量：

`nvram -p`

- [p]rint 以 [x]ML 格式打印存储在 NVRAM 中的所有变量：

`nvram -xp`

- 修改固件变量的值：

`sudo nvram {{name}}="{{value}}"`

- [d]elete 删除一个固件变量：

`sudo nvram -d {{name}}`

- [c]lear 清除所有固件变量：

`sudo nvram -c`

- 从特定的 [x]ML [f]ile 文件设置固件变量：

`sudo nvram -xf {{path/to/file.xml}}`
