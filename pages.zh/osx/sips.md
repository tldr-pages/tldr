# sips

> 苹果脚本可处理图像系统。
> 栅格/查询图像和 ColorSync ICC 配置文件。
> 更多信息：<https://keith.github.io/xcode-man-pages/sips.1.html>。

- 指定输出目录，以便不修改原始文件：

`sips --out {{path/to/out_dir}}`

- 在指定大小下重新采样图像，可能会改变图像的纵横比：

`sips --resampleHeightWidth {{1920}} {{300}} {{image_file.ext}}`

- 重新采样图像，使高度和宽度不超过指定大小（注意大写的 Z）：

`sips --resampleHeightWidthMax {{1920}} {{300}} {{image_file.ext}}`

- 将目录中的所有图像重新采样以适应宽度为 960 像素（遵循纵横比）：

`sips --resampleWidth {{960}} {{path/to/images}}`

- 将图像从 CMYK 转换为 RGB：

`sips --matchTo "/System/Library/ColorSync/Profiles/Generic RGB Profile.icc" {{path/to/image.ext}} {{path/to/out_dir}}`

- 从图像中删除 ColorSync ICC 配置文件：

`sips --deleteProperty profile --deleteColorManagementProperties {{path/to/image_file.ext}}`