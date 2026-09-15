# spottopgm

> SPOT 위성 이미지를 PGM 형식으로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/spottopgm.html>.

- 지정한 SPOT 이미지를 PGM 형식으로 변환:

`spottopgm {{경로/대상/파일.spot}} > {{경로/대상/출력파일.pgm}}`

- 지정한 색상 채널 추출:

`spottopgm -{{1|2|3}} {{경로/대상/파일.spot}} > {{경로/대상/출력파일.pgm}}`

- 입력 이미지에서 지정한 사각형 영역 추출:

`spottopgm {{first_col first_row last_col last_row}} {{경로/대상/파일.spot}} > {{경로/대상/출력파일.pgm}}`
