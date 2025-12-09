# mdatopbm

> Microdesign MDA 파일을 PBM 이미지로 변환.
> 같이 보기: `pbmtomda`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/mdatopbm.html>.

- MDA 파일을 PBM 이미지로 변환:

`mdatopbm {{경로/대상/이미지.mda}} > {{경로/대상/출력.pbm}}`

- 입력 이미지의 색상을 반전:

`mdatopbm -i {{경로/대상/이미지.mda}} > {{경로/대상/출력.pbm}}`

- 입력 이미지의 높이를 두 배로:

`mdatopbm -d {{경로/대상/이미지.mda}} > {{경로/대상/출력.pbm}}`
