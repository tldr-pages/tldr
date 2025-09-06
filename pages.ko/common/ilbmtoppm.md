# ilbmtoppm

> ILBM 파일을 PPM 이미지로 변환:.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ilbmtoppm.html>.

- ILBM 파일을 PPM 이미지로 변환:

`ilbmtoppm {{경로/대상/파일.ilbm}} > {{경로/대상/파일.ppm}}`

- 이미지가 투명한 부분을 "비춰보이게" 하려면 지정된 색상을 사용:

`ilbmtoppm -transparent {{색깔}} {{경로/대상/파일.ilbm}} > {{경로/대상/파일.ppm}}`

- 지정된 청크 ID를 가진 청크를 무시:

`ilbmtoppm -ignore {{chunkID}} {{경로/대상/파일.ilbm}} > {{경로/대상/파일.ppm}}`

- 입력의 투명도 정보를 지정된 PBM 파일에 저장:

`ilbmtoppm -maskfile {{경로/대상/마스크파일.pbm}} {{경로/대상/파일.ilbm}} > {{경로/대상/파일.ppm}}`
