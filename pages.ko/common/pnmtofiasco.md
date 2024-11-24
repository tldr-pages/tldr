# pnmtofiasco

> PNM 이미지를 압축된 FIASCO 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtofiasco.html>.

- PNM 이미지를 압축된 FIASCO 파일로 변환:

`pnmtofiasco {{경로/대상/파일.pnm}} > {{경로/대상/파일.fiasco}}`

- 패턴을 통해 [i]nput 파일 지정:

`pnmtofiasco --image-name "{{img[01-09+1].pnm}}" > {{경로/대상/파일.fiasco}}`

- 압축 품질 지정:

`pnmtofiasco --quality {{품질_수준}} {{경로/대상/파일.pnm}} > {{경로/대상/파일.fiasco}}`

- 지정된 구성 파일에서 사용할 옵션 로드:

`pnmtofiasco --config {{경로/대상/fiascorc}} {{경로/대상/파일.pnm}} > {{경로/대상/파일.fiasco}}`
