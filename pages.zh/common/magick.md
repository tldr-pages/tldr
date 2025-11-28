# magick

> 创建，编辑，组合，转换不同格式的图片文件。
> 这个工具在 ImageMagick 7 以上版本中代替了原 `convert` 命令，如需在 7+ 版本中使用原命令，请查看 `magick convert`。
> 此命令也有关于其子命令的文件，例如：`mogrify`。
> 更多信息：<https://imagemagick.org/script/magick.php>.

- 转换图片格式：

`magick {{路径/到/输入图片.png}} {{路径/到/输出图片.jpg}}`

- 改变图片大小，生成新的副本：

`magick {{路径/到/输入图片.jpg}} -resize {{100x100}} {{路径/到/输出图片.jpg}}`

- 利用当前目录下的所有 JPEG 图片生成一个 GIF 动图：

`magick {{*.jpg}} {{路径/到/GIF文件.gif}}`

- 生成棋盘格图片：

`magick -size {{640x480}} pattern:checkerboard {{路径/到/棋盘格图片.png}}`

- 利用当前目录下的所有 JPEG 图片生成一个 PDF 文件：

`magick {{*.jpg}} -adjoin {{路径/到/PDF文件.pdf}}`
