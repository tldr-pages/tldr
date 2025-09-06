# ppmfade

> 두 개의 PPM 이미지 간의 전환을 생성.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmfade.html>.

- 지정된 효과를 사용하여 두 PPM 이미지([f]irst 및 [l]ast) 간의 전환 생성:

`ppmfade -f {{경로/대상/이미지1.ppm}} -l {{경로/대상/이미지2.ppm}} -{{mix|spread|shift|relief|oil|...}}`

- 지정된 이미지로 시작하여 검은색 단색 이미지로 끝나는 전환 생성:

`ppmfade -f {{경로/대상/이미지.ppm}} -{{mix|spread|shift|relief|oil|...}}`

- 검은색 단색 이미지로 시작하여 지정된 이미지로 끝나는 전환 생성:

`ppmfade -l {{경로/대상/이미지.ppm}} -{{mix|spread|shift|relief|oil|...}}`

- 결과 이미지를 `base.NNNN.ppm` 형식의 파일에 저장 (`NNNN`은 증가하는 숫자):

`ppmfade -f {{경로/대상/이미지1.ppm}} -l {{경로/대상/이미지2.ppm}} -{{mix|spread|shift|relief|oil|...}} -base {{base}}`
