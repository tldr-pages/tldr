# dwebp

> `dwebp`는 WebP 파일을 PNG, PAM, PPM 또는 PGM 이미지로 압축 해제.
> 애니메이션 WebP 파일은 지원되지 않음.
> 더 많은 정보: <https://developers.google.com/speed/webp/docs/dwebp/>.

- WebP 파일을 PNG 파일로 변환:

`dwebp {{경로/대상/입력파일.webp}} -o {{경로/대상/출력파일.png}}`

- WebP 파일을 특정 파일 형식으로 변환:

`dwebp {{경로/대상/입력파일.webp}} -bmp|-tiff|-pam|-ppm|-pgm|-yuv -o {{경로/대상/출력파일}}`

- 가능한 경우, 멀티스레딩을 사용하여 WebP 파일을 변환:

`dwebp {{경로/대상/입력파일.webp}} -o {{경로/대상/출력파일.png}} -mt`

- WebP 파일을 변환하는 동시에, 자르기 및 크기 조정도 가능:

`dwebp {{입력.webp}} -o {{출력.png}} -crop {{x_위치}} {{y_위치}} {{너비}} {{높이;}} -scale {{너비}} {{높이}}`

- WebP 파일을 변환하고 출력을 뒤집음:

`dwebp {{경로/대상/입력파일.webp}} -o {{경로/대상/출력파일.png}} -flip`

- Convert a WebP 파일을 변환하고 디코딩 프로세스 속도를 높이기 위해 인루프 필터링을 사용하지 않음:

`dwebp {{경로/대상/입력파일.webp}} -o {{경로/대상/출력파일.png}} -nofilter`
