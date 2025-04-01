# waifu2x-ncnn-vulkan

> 用于漫画/动画风格图像的图像放大工具，采用 NCNN 神经网络框架。
> 更多信息：<https://github.com/nihui/waifu2x-ncnn-vulkan>.

- 放大图像：

`waifu2x-ncnn-vulkan -i {{path/to/input_file}} -o {{path/to/output_file}}`

- 使用自定义缩放因子并去噪放大图像：

`waifu2x-ncnn-vulkan -i {{path/to/input_file}} -o {{path/to/output_file}} -s {{1|2|4|8|16|32}} -n {{-1|0|1|2|3}}`

- 以特定格式保存放大的图像：

`waifu2x-ncnn-vulkan -i {{path/to/input_file}} -o {{path/to/output_file}} -f {{jpg|png|webp}}`
