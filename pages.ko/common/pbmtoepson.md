# pbmtoepson

> PBM 이미지를 Epson 프린터 그래픽으로 변환.
> 같이 보기: `pbmtoescp2`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtoepson.html>.

- PBM 이미지를 Epson 프린터 그래픽으로 변환:

`pbmtoepson {{경로/대상/이미지.pbm}} > {{경로/대상/출력.epson}}`

- 출력의 프린터 프로토콜 지정:

`pbmtoepson -protocol {{escp9|escp}} {{경로/대상/이미지.pbm}} > {{경로/대상/출력.epson}}`

- 출력의 가로 DPI 지정:

`pbmtoepson -dpi {{60|72|80|90|120|144|240}} {{경로/대상/이미지.pbm}} > {{경로/대상/출력.epson}}`
