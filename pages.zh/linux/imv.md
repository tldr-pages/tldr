# imv

> 用于 Wayland 和 X11 的命令行图像查看器，主要针对平铺窗口管理器。
> 支持多种格式，包括 Photoshop (PSD)。
> 更多信息：<https://sr.ht/~exec64/imv>.

- 查看多张图片：

`imv {{path/to/image1.ext path/to/image2.ext ...}}`

- 全屏模式查看图片：

`imv -f {{path/to/image.ext}}`

- 从指定路径递归地查看图片：

`imv -r --slideshow {{path/to/path}}`

- 通过 `stdin` 打开多张图片：

`find . -type f -name "{{*.svg}}" | imv`

- 从目录创建幻灯片，每张图片显示 10 秒：

`imv -t 10 {{path/to/directory}}`

- 查看来自网络的多张图片：

`curl -Osw '%{filename_effective}\n' '{{http://www.example.com/[1-10].jpg}}' | imv`
