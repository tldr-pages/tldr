# waifu2x-ncnn-vulkan

> NCNN neurális hálózati keretrendszerrel készült kép-felskálázó manga/anime stílusú képekhez. További információ: <https://github.com/nihui/waifu2x-ncnn-vulkan>.

- Egy kép felskálázása:

`waifu2x-ncnn-vulkan -i {{path/to/input_file}} -o {{path/to/output_file}}`

- Egy kép felskálázása egy egyéni méretezési tényezővel és denzikalizálása:

`waifu2x-ncnn-vulkan -i {{path/to/input_file}} -o {{path/to/output_file}} -s {{1|2|4|8|16|32}} -n {{-1|0|1|2|3}}`

- A felskálázott kép mentése egy adott formátumban:

`waifu2x-ncnn-vulkan -i {{path/to/input_file}} -o {{path/to/output_file}} -f {{jpg|png|webp}}`
