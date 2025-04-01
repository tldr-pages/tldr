# sxiv

> 简单的 X 图像查看器。
> 更多信息：<https://github.com/muennich/sxiv>.

- 打开一个图像：

`sxiv {{path/to/image}}`

- 以全屏模式打开一个图像：

`sxiv -f {{path/to/file}}`

- 从 `stdin` 读取文件名，以换行分隔的图像列表形式打开图像：

`echo {{path/to/file}} | sxiv -i`

- 以幻灯片形式打开一个或多个图像：

`sxiv -S {{seconds}} {{path/to/image1 path/to/image2}}`

- 以缩略图模式打开一个或多个图像：

`sxiv -t {{path/to/image1 path/to/image2}}`
