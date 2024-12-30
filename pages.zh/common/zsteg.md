# zsteg

> 针对PNG和BMP文件格式的隐写检测工具。
> 它可以检测最低有效位（LSB）隐写术、ZLIB压缩数据、OpenStego、Camouflage以及使用厄拉托斯特尼斯集合的LSB。
> 更多信息请访问：<https://github.com/zed-0xff/zsteg>。

- 检测PNG中的嵌入数据：

`zsteg {{path/to/image.png}}`

- 检测BMP图像中的嵌入数据，使用所有已知方法：

`zsteg --all {{path/to/image.bmp}}`

- 检测PNG中的嵌入数据，垂直迭代像素并优先考虑最高有效位（MSB）：

`zsteg --msb --order yx {{path/to/image.png}}`

- 检测BMP图像中的嵌入数据，指定要考虑的位：

`zsteg --bits {{1,2,3|1-3}} {{path/to/image.bmp}}`

- 检测PNG中的嵌入数据，仅提取素数像素并反转位：

`zsteg --prime --invert {{path/to/image.png}}`

- 检测BMP图像中的嵌入数据，指定要找到的字符串的最小长度和查找模式：

`zsteg --min-str-len {{10}} --strings {{first|all|longest|none}} {{path/to/image.bmp}}`