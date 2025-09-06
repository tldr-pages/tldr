# pamundice

> 여러 개의 Netpbm 이미지를 하나로 결합.
> 같이 보기: `pamdice`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamundice.html>.

- `printf` 스타일의 파일 이름 표현과 일치하는 이미지 결합. 특정 크기의 그리드를 가정:

`pamundice {{파일이름_%1d_%1a.ppm}} {{[-a|-across]}} {{그리드_너비}} {{[-d|-down]}} {{그리드_높이}} > {{경로/대상/출력.ppm}}`

- 타일이 지정된 양만큼 수평 및 수직으로 겹친다고 가정:

`pamundice {{파일이름_%1d_%1a.ppm}} {{[-a|-across]}} {{x_값}} {{[-d|-down]}} {{y_값}} {{[-ho|-hoverlap]}} {{값}} {{[-vo|-voverlap]}} {{값}} > {{경로/대상/출력.ppm}}`

- 결합할 이미지를 한 줄에 하나의 파일 이름이 있는 텍스트 파일로 지정:

`pamundice {{[-l|-listfile]}} {{경로/대상/파일.txt}} {{[-a|-across]}} {{x_값}} {{[-d|-down]}} {{y_값}} > {{경로/대상/출력.ppm}}`
