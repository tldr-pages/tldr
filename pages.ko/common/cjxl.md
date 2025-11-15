# cjxl

> 이미지를 JPEG XL로 압축.
> 허용되는 입력 확장자는 PNG, APNG, GIF, JPEG, EXR, PPM, PFM, PAM, PGX 및 JXL입니다.
> 더 많은 정보: <https://github.com/libjxl/libjxl>.

- 이미지를 JPEG XL로 변환:

`cjxl {{경로/대상/이미지.ext}} {{경로/대상/출력.jxl}}`

- 품질에 손실이 없게하고 결과 이미지의 압축을 최대화함:

`cjxl --distance 0 --effort 9 {{경로/대상/이미지.ext}} {{경로/대상/출력.jxl}}`

- 매우 상세한 도움말 페이지를 표시:

`cjxl {{[-h -v -v -v -v|--help --verbose --verbose --verbose --verbose]}}`
