# pamditherbw

> 그레이스케일 이미지에 디더링을 적용하여 원래의 그레이스케일과 동일하게 보이는 흑백 픽셀 패턴으로 변환.
> 같이 보기: `pbmreduce`.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamditherbw.html>.

- PGM 이미지를 읽고 디더링을 적용하여 파일로 저장:

`pamditherbw {{경로/대상/image.pgm}} > {{경로/대상/파일.pgm}}`

- 지정된 양자화 방법 사용:

`pamditherbw -{{floyd|fs|atkinson|threshold|hilbert|...}} {{경로/대상/image.pgm}} > {{경로/대상/파일.pgm}}`

- atkinson 양자화 방법과 지정된 시드를 사용하여 의사 난수 생성기 사용:

`pamditherbw {{[-a|-atkinson]}} {{[-r|-randomseed]}} {{1337}} {{경로/대상/image.pgm}} > {{경로/대상/파일.pgm}}`

- 특정 형태의 임계값 처리를 수행하는 양자화 방법을 위한 임계값 지정:

`pamditherbw -{{fs|atkinson|thresholding}} {{[-va|-value]}} {{0.3}} {{경로/대상/image.pgm}} > {{경로/대상/파일.pgm}}`
