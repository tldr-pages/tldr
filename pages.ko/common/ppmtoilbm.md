# ppmtoilbm

> PPM 이미지를 ILBM 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtoilbm.html>.

- PPM 이미지를 ILBM 파일로 변환:

`ppmtoilbm {{경로/대상/파일.ppm}} > {{경로/대상/파일.ilbm}}`

- ILBM 파일에 최대 {{n}}개의 플레인 작성하고, 이 수를 초과하면 HAM/24비트/직접 색상 파일 생성:

`ppmtoilbm -maxplanes {{n}} -{{hamif|24if|dcif}} {{경로/대상/파일.ppm}} > {{경로/대상/파일.ilbm}}`

- 정확히 {{n}}개의 플레인으로 ILBM 파일 생성:

`ppmtoilbm -fixplanes {{n}} {{경로/대상/파일.ppm}} > {{경로/대상/파일.ilbm}}`

- 사용할 압축 방법 선택:

`ppmtoilbm -{{compress|nocompress|savemem}} {{경로/대상/파일.ppm}} > {{경로/대상/파일.ilbm}}`
