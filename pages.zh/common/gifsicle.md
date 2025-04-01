# gifsicle

> 创建、编辑、操作和获取 GIF 文件的信息。
> 更多信息：<https://www.lcdf.org/gifsicle>.

- 将 GIF 优化为新文件：

`gifsicle {{path/to/input.gif}} {{[-O|--optimize=]}}3 {{[-o|--output]}} {{path/to/output.gif}}`

- 使用批处理模式（直接修改每个给定的文件）并取消优化 GIF：

`gifsicle {{[-b|--batch]}} {{path/to/input.gif}} {{[-U|--unoptimize]}}`

- 从 GIF 中提取一帧：

`gifsicle {{path/to/input.gif}} '#{{0}}' > {{path/to/first_frame.gif}}`

- 从选定的 GIF 文件创建动画 GIF：

`gifsicle {{*.gif}} {{[-d|--delay]}} {{10}} {{[-l|--loop]}} > {{path/to/output.gif}}`

- 使用有损压缩减少文件大小：

`gifsicle {{[-b|--batch]}} {{path/to/input.gif}} {{[-O|--optimize=]}}3 --lossy={{100}} {{[-k|--colors]}} {{16}} {{[-f|--dither]}}`

- 从 GIF 中删除前 10 帧和第 20 帧之后的所有帧：

`gifsicle {{[-b|--batch]}} {{path/to/input.gif}} --delete '#{{0-9}}' '#{{20-}}'`

- 通过裁剪、缩放、水平翻转和旋转来修改所有帧：

`gifsicle {{[-b|--batch]}} --crop {{starting_x}},{{starting_y}}+{{rect_width}}x{{rect_height}} --scale {{0.25}} --flip-horizontal --rotate-{{90|180|270}} {{path/to/input.gif}}`