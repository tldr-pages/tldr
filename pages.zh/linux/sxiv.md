# sxiv

> 简单的 X 图片查看器。
> 更多信息：<https://github.com/muennich/sxiv>。

- 打开一张图片：

`sxiv {{path/to/image}}`

- 以全屏模式打开一张图片：

`sxiv -f {{path/to/file}}`

- 打开一个以换行符分隔的图片列表，从 `stdin` 读取文件名：

`echo {{path/to/file}} | sxiv -i`

- 以幻灯片形式打开一张或多张图片：

`sxiv -S {{seconds}} {{path/to/image1 path/to/image2}}`

- 以缩略图模式打开一张或多张图片：

`sxiv -t {{path/to/image1 path/to/image2}}`