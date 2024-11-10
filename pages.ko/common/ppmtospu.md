# ppmtospu

> PPM 파일을 Atari Spectrum 512 이미지로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtospu.html>.

- PPM 파일을 Atari Spectrum 512 이미지로 변환:

`ppmtospu {{경로/대상/입력.ppm}} > {{경로/대상/출력.spu}}`

- 지정된 크기의 디더링 매트릭스를 사용 (0은 디더링 없음):

`ppmtospu -d{{0|2|4}} {{경로/대상/입력.ppm}} > {{경로/대상/출력.spu}}`
