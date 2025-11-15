# pbmtonokia

> PBM 이미지를 Nokia의 스마트 메시징 형식 중 하나로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtonokia.html>.

- PBM 이미지를 Nokia 운영자 로고로 변환하여 헥스 코드로 출력:

`pbmtonokia -fmt NEX_NOL -net {{네트워크_운영자_코드}} {{경로/대상/이미지.pbm}} > {{경로/대상/출력.hex}}`

- PBM 이미지를 Nokia 그룹 그래픽으로 변환하여 헥스 코드로 출력:

`pbmtonokia -fmt NEX_NGG {{경로/대상/이미지.pbm}} > {{경로/대상/출력.hex}}`

- PBM 이미지를 지정된 텍스트와 함께 Nokia 그림 메시지로 변환하여 헥스 코드로 출력:

`pbmtonokia -fmt NEX_NPM -txt {{텍스트_메시지}} {{경로/대상/이미지.pbm}} > {{경로/대상/출력.hex}}`

- PBM 이미지를 Nokia 운영자 로고로 변환하여 NOL 파일로 출력:

`pbmtonokia -fmt NOL {{경로/대상/이미지.pbm}} > {{경로/대상/출력.nol}}`

- PBM 이미지를 Nokia 그룹 그래픽으로 변환하여 NGG 파일로 출력:

`pbmtonokia -fmt NGG {{경로/대상/이미지.pbm}} > {{경로/대상/출력.ngg}}`

- PBM 이미지를 Nokia 그림 메시지로 변환하여 NPM 파일로 출력:

`pbmtonokia -fmt NPM {{경로/대상/이미지.pbm}} > {{경로/대상/출력.npm}}`
