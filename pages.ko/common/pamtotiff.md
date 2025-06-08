# pamtotiff

> PAM 이미지를 TIFF 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamtotiff.html>.

- PAM 이미지를 TIFF 이미지로 변환:

`pamtotiff {{경로/대상/입력_파일.pam}} > {{경로/대상/출력_파일.tiff}}`

- 출력 파일의 압축 방식을 명시적으로 지정:

`pamtotiff -{{none|packbits|lzw|g3|g4|flate|adobeflate}} {{경로/대상/입력_파일.pam}} > {{경로/대상/출력_파일.tiff}}`

- 입력 이미지가 그레이스케일일지라도 항상 컬러 TIFF 이미지를 생성:

`pamtotiff {{[-c|-color]}} {{경로/대상/입력_파일.pam}} > {{경로/대상/출력_파일.tiff}}`
