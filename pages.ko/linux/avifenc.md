# avifenc

> AV1 이미지 파일 포맷 (AVIF) 인코더.
> 더 많은 정보: <https://aomediacodec.github.io/av1-avif/>.

- 특정 PNG 이미지를 AVIF로 변환:

`avifenc {{경로/대상/입력.png}} {{경로/대상/출력.avif}}`

- 특정 속도로 인코딩 (6=기본, 0=가장 느림, 10=가장 빠름):

`avifenc --speed {{2}} {{경로/대상/입력.png}} {{경로/대상/출력.avif}}`
