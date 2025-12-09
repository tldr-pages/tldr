# ppmhist

> PPM 이미지에 포함된 색상의 히스토그램을 출력.
> 같이 보기: `pgmhist`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmhist.html>.

- 사람이 읽을 수 있는 형식으로 히스토그램 생성:

`ppmhist -nomap {{경로/대상/이미지.ppm}}`

- 이미지의 색상 히스토그램을 주석으로 포함한 컬러맵의 PPM 파일 생성:

`ppmhist -map {{경로/대상/이미지.ppm}}`

- 버전 표시:

`ppmhist -version`
