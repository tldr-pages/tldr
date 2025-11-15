# pbmtomda

> PBM 이미지를 Microdesign MDA 파일로 변환.
> 같이 보기: `mdatopbm`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtomda.html>.

- PBM 이미지를 MDA 파일로 변환:

`pbmtomda {{경로/대상/이미지.pbm}} > {{경로/대상/출력.mda}}`

- 입력 이미지의 색상을 반전:

`pbmtomda -i {{경로/대상/이미지.pbm}} > {{경로/대상/출력.mda}}`

- 입력 이미지의 높이를 절반으로 줄임:

`pbmtomda -d {{경로/대상/이미지.pbm}} > {{경로/대상/출력.mda}}`
