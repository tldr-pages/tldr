# pdftoppm

> PDF 문서 페이지를 Portable Pixmap(이미지 형식)으로 변환.
> 더 많은 정보: <https://manned.org/pdftoppm>.

- 변환할 페이지 범위 지정 (N-첫 번째 페이지, M-마지막 페이지):

`pdftoppm -f {{N}} -l {{M}} {{경로/대상/파일.pdf}} {{이미지_이름_접두사}}`

- PDF의 첫 번째 페이지만 변환:

`pdftoppm -singlefile {{경로/대상/파일.pdf}} {{이미지_이름_접두사}}`

- 모노크롬 PBM 파일 생성 (컬러 PPM 파일 대신):

`pdftoppm -mono {{경로/대상/파일.pdf}} {{이미지_이름_접두사}}`

- 그레이스케일 PGM 파일 생성 (컬러 PPM 파일 대신):

`pdftoppm -gray {{경로/대상/파일.pdf}} {{이미지_이름_접두사}}`

- PPM 파일 대신 PNG 파일 생성:

`pdftoppm -png {{경로/대상/파일.pdf}} {{이미지_이름_접두사}}`
