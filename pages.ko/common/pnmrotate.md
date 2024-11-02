# pnmrotate

> PNM 이미지를 회전.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmrotate.html>.

- PNM 이미지를 일정 각도(기준은 도, 반시계 방향)로 회전:

`pnmrotate {{각도}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`

- 입력 이미지 회전 시 노출되는 배경색 지정:

`pnmrotate -background {{색상}} {{각도}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`

- 성능을 향상시키지만 품질을 낮추는 안티앨리어싱 비활성화:

`pnmrotate -noantialias {{각도}} {{경로/대상/입력.pnm}} > {{경로/대상/출력.pnm}}`
