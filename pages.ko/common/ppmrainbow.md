# ppmrainbow

> 무지개 생성.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmrainbow.html>.

- 지정한 색상들로 구성된 무지개 생성:

`ppmrainbow {{색상1 색상2 ...}} > {{경로/대상/출력_파일.ppm}}`

- 출력 크기를 픽셀로 지정:

`ppmrainbow -width {{너비}} -height {{높이}} {{색상1 색상2 ...}} > {{경로/대상/출력_파일.ppm}}`

- 마지막 색상으로 무지개 끝내기, 첫 번째 색상 반복하지 않기:

`ppmrainbow -norepeat {{색상1 색상2 ...}} > {{경로/대상/출력_파일.ppm}}`
