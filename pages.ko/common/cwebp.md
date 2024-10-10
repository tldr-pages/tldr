# cwebp

> 이미지 파일을 WebP 파일로 압축.
> 더 많은 정보: <https://developers.google.com/speed/webp/docs/cwebp>.

- 기본 설정 (q = 75)을 사용하여 WebP 파일을 출력([o]utput) 파일로 압축:

`cwebp {{경로/대상/이미지_파일}} -o {{경로/대상/출력파일.webp}}`

- 최고 품질([q]uality)과 최대 파일 크기로 WebP 파일을 압축:

`cwebp {{경로/대상/이미지_파일}} -o {{경로/대상/출력파일.webp}} -q {{100}}`

- 최저 품질([q]uality)과 최소 파일 크기로 WebP 파일을 압축:

`cwebp {{경로/대상/이미지_파일}} -o {{경로/대상/출력파일.webp}} -q {{0}}`

- WebP 파일을 압축하고 이미지에 크기 조정을 적용:

`cwebp {{경로/대상/이미지_파일}} -o {{경로/대상/출력파일.webp}} -resize {{width}} {{height}}`

- WebP 파일을 압축하고 알파 채널 정보를 삭제:

`cwebp {{경로/대상/이미지_파일}} -o {{경로/대상/출력파일.webp}} -noalpha`
