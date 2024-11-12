# pnmgamma

> PNM 이미지에 감마 보정 수행.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmgamma.html>.

- 이미지를 BT.709 휘도에서 방사선 또는 sRGB 휘도로 변환:

`pnmgamma -{{bt709tolinear|bt709tosrgb}} {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`

- 이미지를 방사선 또는 sRGB 휘도에서 BT.709 휘도로 변환:

`pnmgamma -{{lineartobt709|srgbtobt709}} {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`

- 감마 전송 함수에 사용될 감마 값 지정:

`pnmgamma -gamma {{값}} {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`

- 색 구성 요소별로 감마 전송 함수에 사용될 감마 값 지정:

`pnmgamma -rgamma {{값}} -ggamma {{값}} -bgamma {{값}} {{경로/대상/이미지.pnm}} > {{경로/대상/출력.pnm}}`
