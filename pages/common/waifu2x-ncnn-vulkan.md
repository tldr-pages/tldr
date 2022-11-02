# waifu2x-ncnn-vulkan

> Image upscaler for manga/anime-style images using NCNN neural network framework.
> Runs fast on Intel / AMD / Nvidia / Apple-Silicon with Vulkan API.
> More information: <https://github.com/nihui/waifu2x-ncnn-vulkan>.

- Upscale image:

`waifu2x-ncnn-vulkan -i {{path/to/file}} -o {{path/to/output/file}}`

- Upscale image by the scale factor of 4 and denoise it:

`waifu2x-ncnn-vulkan -i path/to/file -o path/to/output/file -s 4 -n 3`

- Save upscaled image in JPEG format:

`waifu2x-ncnn-vulkan -i path/to/file -o path/to/output/file -f jpg`
