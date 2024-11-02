# pnmtopclxl

> PNM 파일을 HP LaserJet PCL XL 프린터 스트림으로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtopclxl.html>.

- PNM 파일을 HP LaserJet PCL XL 프린터 스트림으로 변환:

`pnmtopclxl {{경로/대상/입력1.pnm 경로/대상/입력2.pnm ...}} > {{경로/대상/출력.pclxl}}`

- 각 이미지의 왼쪽 상단 모서리에서 이미지 해상도 및 페이지 위치 지정:

`pnmtopclxl -dpi {{해상도}} -xoffs {{x_오프셋}} -yoffs {{y_오프셋}} {{경로/대상/입력1.pnm 경로/대상/입력2.pnm ...}} > {{경로/대상/출력.pclxl}}`

- 지정된 용지 형식에 대한 양면 프린터 스트림 생성:

`pnmtopclxl -duplex {{세로|가로}} -format {{letter|legal|a3|a4|a5|...}} {{경로/대상/입력1.pnm 경로/대상/입력2.pnm ...}} > {{경로/대상/출력.pclxl}}`
