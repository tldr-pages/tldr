# pnmtoxwd

> PNM 파일을 X11 윈도우 덤프 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtoxwd.html>.

- PNM 이미지 파일을 XWD로 변환:

`pnmtoxwd {{경로/대상/입력_파일.pnm}} > {{경로/대상/출력_파일.xwd}}`

- DirectColor 형식으로 출력 생성:

`pnmtoxwd -directcolor {{경로/대상/입력_파일.pnm}} > {{경로/대상/출력_파일.xwd}}`

- 출력의 색상 깊이를 b 비트로 설정:

`pnmtoxwd -pseudodepth {{b}} {{경로/대상/입력_파일.pnm}} > {{경로/대상/출력_파일.xwd}}`
