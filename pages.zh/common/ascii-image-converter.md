# ascii-image-converter

> 将图像转换为 ASCII。
> 更多信息：<https://github.com/TheZoraiz/ascii-image-converter#cli-usage>.

- 将图像转换为 ASCII：

`ascii-image-converter {{路径/到/图像|URL}}`

- 为输出添加颜色：

`ascii-image-converter {{[-C|--color]}} {{路径/到/图像|URL}}`

- 使用盲文创建一个阈值化图像（如果图像几乎不可见，可以尝试更改终端字体）：

`ascii-image-converter {{[-b|--braille]}} {{路径/到/图像|URL}}`

- 使用盲文创建一个抖动图像（如果图像几乎不可见，可以尝试更改终端字体）：

`ascii-image-converter {{[-b|--braille]}} --dither {{路径/到/图像|URL}}`

- 以反色方式显示图像：

`ascii-image-converter {{[-Cn|--color --negative]}} {{路径/到/图像|URL}}`

- 使用更宽的字符范围来显示图像（可能会提升图像的准确度）：

`ascii-image-converter {{[-c|--complex]}} {{路径/到/图像|URL}}`
