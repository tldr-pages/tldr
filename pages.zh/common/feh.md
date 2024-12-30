# feh

> 轻量级图像查看工具。
> 更多信息：<https://feh.finalrewind.org>。

- 本地或通过 URL 查看图像：

`feh {{path/to/images}}`

- 递归查看图像：

`feh --recursive {{path/to/images}}`

- 无窗口边框查看图像：

`feh --borderless {{path/to/images}}`

- 最后一个图像后退出：

`feh --cycle-once {{path/to/images}}`

- 使用特定的幻灯片循环延迟：

`feh --slideshow-delay {{seconds}} {{path/to/images}}`

- 使用特定的壁纸模式（居中、填充、最大化、缩放或平铺）：

`feh --bg-{{center|fill|max|scale|tile}} {{path/to/image}}`

- 创建一个目录中所有图像的蒙太奇，并输出为新图像：

`feh --montage --thumb-height {{150}} --thumb-width {{150}} --index-info "{{%nn%wx%h}}" --output {{path/to/montage_image.png}}`