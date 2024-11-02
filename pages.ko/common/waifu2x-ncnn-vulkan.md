# waifu2x-ncnn-vulkan

> NCNN 신경망 프레임워크를 사용하여 만화/애니메이션 스타일 이미지의 해상도를 높이는 도구.
> 더 많은 정보: <https://github.com/nihui/waifu2x-ncnn-vulkan>.

- 이미지 해상도 높이기:

`waifu2x-ncnn-vulkan -i {{경로/대상/입력_파일}} -o {{경로/대상/출력_파일}}`

- 사용자 정의 배율로 이미지 해상도 높이고 노이즈 제거:

`waifu2x-ncnn-vulkan -i {{경로/대상/입력_파일}} -o {{경로/대상/출력_파일}} -s {{1|2|4|8|16|32}} -n {{-1|0|1|2|3}}`

- 특정 형식으로 해상도 높인 이미지 저장:

`waifu2x-ncnn-vulkan -i {{경로/대상/입력_파일}} -o {{경로/대상/출력_파일}} -f {{jpg|png|webp}}`
