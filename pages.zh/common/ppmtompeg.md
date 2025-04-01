# ppmtompeg

> 编码 MPEG-1 流。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtompeg.html>.

- 使用参数文件指定输入和输出，生成 MPEG-1 流：

`ppmtompeg {{path/to/parameter_file}}`

- 仅编码指定编号的 GOP：

`ppmtompeg -gop {{gop_num}} {{path/to/parameter_file}}`

- 指定要编码的第一帧和最后一帧：

`ppmtompeg -frames {{first_frame}} {{last_frame}} {{path/to/parameter_file}}`

- 将多个 MPEG 帧组合成一个 MPEG-1 流：

`ppmtompeg -combine_frames {{path/to/parameter_file}}`
