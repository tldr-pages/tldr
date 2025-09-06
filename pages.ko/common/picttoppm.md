# picttoppm

> Macintosh PICT 파일을 PPM 이미지로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/picttoppm.html>.

- PICT 파일을 PPM 이미지로 변환:

`picttoppm {{경로/대상/파일.pict}} > {{경로/대상/파일.ppm}}`

- PICT 파일의 모든 이미지를 최대 해상도로 출력하도록 강제:

`picttoppm -fullres {{경로/대상/파일.pict}} > {{경로/대상/파일.ppm}}`

- 입력 파일에 PICT 헤더가 포함되어 있다고 가정하지 않고, quickdraw 작업만 실행:

`picttoppm -noheader -quickdraw {{경로/대상/파일.pict}} > {{경로/대상/파일.ppm}}`
