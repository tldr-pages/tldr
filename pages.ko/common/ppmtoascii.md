# ppmtoascii

> PPM 이미지를 ANSI 터미널 색상 코드를 사용하여 ASCII 이미지로 변환.
> 같이 보기: `ppmtoterm`, `pbmtoascii`, `pbmto4425`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtoascii.html>.

- 1x2 픽셀 영역을 하나의 문자로 결합하여 PPM 이미지를 ASCII 이미지로 변환:

`ppmtoascii {{경로/대상/입력.ppm}} > {{경로/대상/출력.txt}}`

- 2x4 픽셀 영역을 하나의 문자로 결합하여 PPM 이미지를 ASCII 이미지로 변환:

`ppmtoascii -2x4 {{경로/대상/입력.ppm}} > {{경로/대상/출력.txt}}`
