# waifu2x-ncnn-vulkan

> 使用 NCNN 神经网络框架的漫画/动漫风格图像放大器。
> 更多信息：<https://github.com/nihui/waifu2x-ncnn-vulkan>。

- 放大图像：

`waifu2x-ncnn-vulkan -i {{路径/到/输入文件}} -o {{路径/到/输出文件}}`

- 按自定义缩放因子放大图像并去噪：

`waifu2x-ncnn-vulkan -i {{路径/到/输入文件}} -o {{路径/到/输出文件}} -s {{1|2|4|8|16|32}} -n {{-1|0|1|2|3}}`

- 以特定格式保存放大的图像：

`waifu2x-ncnn-vulkan -i {{路径/到/输入文件}} -o {{路径/到/输出文件}} -f {{jpg|png|webp}}`