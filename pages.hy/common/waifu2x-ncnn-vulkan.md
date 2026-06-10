# waifu2x-ncnn-vulkan

> Պատկերի բարձրացում մանգայի/անիմե ոճի պատկերների համար՝ օգտագործելով NCNN նեյրոնային ցանցի շրջանակը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/nihui/waifu2x-ncnn-vulkan>:.

- Պատկերի բարձրացում.:

`waifu2x-ncnn-vulkan -i {{path/to/input_file}} -o {{path/to/output_file}}`

- Բարձրացրեք պատկերը հարմարեցված մասշտաբի գործակցով և ջնջեք այն.:

`waifu2x-ncnn-vulkan -i {{path/to/input_file}} -o {{path/to/output_file}} -s {{1|2|4|8|16|32}} -n {{-1|0|1|2|3}}`

- Պահպանեք բարձրացված պատկերը հատուկ ձևաչափով.:

`waifu2x-ncnn-vulkan -i {{path/to/input_file}} -o {{path/to/output_file}} -f {{jpg|png|webp}}`
