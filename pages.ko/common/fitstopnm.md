# fitstopnm

> FITS(Flexible Image Transport System) 파일을 PNM 이미지로 변환.
> 참조: `pamtofits`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/fitstopnm.html>.

- FITS 파일을 PNM 이미지로 변환:

`fitstopnm {{경로/대상/파일.fits}} > {{경로/대상/출력파일.pnm}}`

- FITS 파일의 세 번째 축의 지정된 위치에서 이미지를 변환:

`fitstopnm -image {{z_position}} {{경로/대상/파일.fits}} > {{경로/대상/출력파일.pnm}}`
