# rasttopnm

> Sun 래스터 파일을 PNM 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/rasttopnm.html>.

- RAST 이미지를 PNM 파일로 변환:

`rasttopnm {{경로/대상/입력.rast}} > {{경로/대상/출력.pnm}}`

- 색상 값이 있는 경우 래스터의 색상 맵 인덱스를 사용:

`rasttopnm -index {{경로/대상/입력.rast}} > {{경로/대상/출력.pnm}}`
