# xwdtopnm

> X11 또는 X10 윈도우 덤프 파일을 PNM으로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/xwdtopnm.html>.

- XWD 이미지 파일을 PBM으로 변환:

`xwdtopnm {{경로/대상/입력_파일.xwd}} > {{경로/대상/출력_파일.pnm}}`

- 변환 과정에 대한 정보 표시:

`xwdtopnm -verbose {{경로/대상/입력_파일.xwd}} > {{경로/대상/출력_파일.pnm}}`

- 입력 파일의 X11 헤더 내용 표시:

`xwdtopnm -headerdump {{경로/대상/입력_파일.xwd}} > {{경로/대상/출력_파일.pnm}}`
