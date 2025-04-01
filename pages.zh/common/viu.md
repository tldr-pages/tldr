# viu

> 在终端查看图像。
> 更多信息：<https://github.com/atanunq/viu>.

- 渲染图像或动画 GIF：

`viu {{path/to/file}}`

- 使用 `curl` 从互联网渲染图像或 GIF：

`curl -s {{https://example.com/image.png}} | viu -`

- 渲染带有透明背景的图像：

`viu -t {{path/to/file}}`

- 以指定的宽度和高度（以像素为单位）渲染图像：

`viu -w {{width}} -h {{height}} {{path/to/file}}`

- 渲染图像或 GIF 并显示文件名：

`viu -n {{path/to/file}}`
