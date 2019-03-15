# sips

> 苹果的处理文件脚本系统.
> 光栅/查询图像 和 颜色同步 ICC 配置文件.

- S指定一个输出目录,这样原始文件就不会被修改:

`sips --out {{目标/文件夹/输出文件夹}}`

- 以指定的大小对图像重新采样，图像纵横比可能会更改:

`sips -z {{1920}} {{300}} {{图片文件.扩展名}}`

- 对图像重新取样,使高度和宽度不大于指定的大小（注意大写Z）:

`sips -Z {{1920}} {{300}} {{图片文件.扩展名}}`

- 对目录中的所有图像重新取样，以适应960px的宽度（保持纵横比）:

`sips --resampleWidth {{960}} {{目标/文件夹/所有图片文件}}`

- 将图像从 CMYK 转换为 RGB:

`sips --matchTo '/System/Library/ColorSync/Profiles/Generic RGB Profile.icc' {{目标/文件夹/图片.扩展}} {{目标/文件夹/输出文件夹}}`

- 从图像中删除ColorSync ICC配置:

`sips -d profile --deleteColorManagementProperties {{目标/文件夹/图片.扩展}}`
