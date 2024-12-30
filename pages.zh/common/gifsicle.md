# gifsicle

> 创建、编辑、操作和获取GIF文件的信息。
> 更多信息：<https://www.lcdf.org/gifsicle>。

- 将GIF优化为新文件：

`gifsicle {{path/to/input.gif}} --optimize=3 -o {{path/to/output.gif}}`

- 使用[b]atch模式（就地修改每个给定文件）并取消优化GIF：

`gifsicle -b {{path/to/input.gif}} --unoptimize`

- 从GIF中提取帧：

`gifsicle {{path/to/input.gif}} '#{{0}}' > {{path/to/first_frame.gif}}`

- 从选定的GIF制作GIF动画：

`gifsicle {{*.gif}} --delay={{10}} --loop > {{path/to/output.gif}}`

- 使用有损压缩减少文件大小：

`gifsicle -b {{path/to/input.gif}} --optimize=3 --lossy={{100}} --colors={{16}} --dither`

- 删除GIF的前10帧和第20帧后的所有帧：

`gifsicle -b {{path/to/input.gif}} --delete '#{{0-9}}' '#{{20-}}'`

- 通过裁剪为矩形、改变比例、翻转和旋转来修改所有帧：

`gifsicle -b --crop {{starting_x}},{{starting_y}}+{{rect_width}}x{{rect_height}} --scale {{0.25}} --flip-horizontal --rotate-{{90|180|270}} {{path/to/input.gif}}`