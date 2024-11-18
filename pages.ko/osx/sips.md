# sips

> Apple Scriptable Image Processing System.
> 래스터/쿼리 이미지 및 ColorSync ICC 프로필.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/sips.1.html>.

- 원본이 수정되지 않도록 출력 디렉터리 지정:

`sips --out {{경로/대상/출력_폴더}}`

- 지정된 크기로 이미지 리샘플링 (이미지 비율이 변경될 수 있음):

`sips --resampleHeightWidth {{1920}} {{300}} {{이미지_파일.ext}}`

- 높이와 너비가 지정된 크기를 초과하지 않도록 이미지 리샘플링 (대문자 Z 주의):

`sips --resampleHeightWidthMax {{1920}} {{300}} {{이미지_파일.ext}}`

- 디렉터리 내 모든 이미지를 960px 너비에 맞게 리샘플링 (비율 유지):

`sips --resampleWidth {{960}} {{경로/대상/이미지}}`

- 이미지 색상을 CMYK에서 RGB로 변환:

`sips --matchTo "/System/Library/ColorSync/Profiles/Generic RGB Profile.icc" {{경로/대상/이미지.ext}} {{경로/대상/출력_폴더}}`

- 이미지에서 ColorSync ICC 프로필 제거:

`sips --deleteProperty profile --deleteColorManagementProperties {{경로/대상/이미지_파일.ext}}`
