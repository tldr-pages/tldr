# zsteg

> 用于 PNG 和 BMP 文件格式的隐写术检测工具。
> 它检测 LSB 隐写术、ZLIB 压缩数据、OpenStego、Camouflage 和包含 Eratosthenes 集的 LSB。
> 更多信息：<https://github.com/zed-0xff/zsteg>.

- 检测 PNG 文件中的嵌入数据：

`zsteg {{路径/到/image.png}}`

- 使用所有已知方法检测 BMP 图像中的嵌入数据：

`zsteg --all {{路径/到/image.bmp}}`

- 检测 PNG 中的嵌入数据，以垂直方式遍历像素并优先使用 MSB：

`zsteg --msb --order yx {{路径/到/image.png}}`

- 在 BMP 图像中检测嵌入数据，指定要考虑的位：

`zsteg --bits {{1,2,3|1-3}} {{路径/到/image.bmp}}`

- 检测 PNG 文件中的嵌入数据，仅提取素数像素并反转位：

`zsteg --prime --invert {{路径/到/image.png}}`

- 检测 BMP 图像中的嵌入数据，指定要找到的字符串的最小长度和查找模式：

`zsteg --min-str-len {{10}} --strings {{first|all|longest|none}} {{路径/到/image.bmp}}`
