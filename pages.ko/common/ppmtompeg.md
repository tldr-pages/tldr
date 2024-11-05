# ppmtompeg

> MPEG-1 스트림 인코딩.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtompeg.html>.

- 입력 및 출력을 지정하는 매개 변수 파일을 사용하여 MPEG-1 스트림 생성:

`ppmtompeg {{경로/대상/매개_변수_파일}}`

- 지정된 번호의 GOP만 인코딩:

`ppmtompeg -gop {{gop_번호}} {{경로/대상/매개_변수_파일}}`

- 인코딩할 첫 번째 및 마지막 프레임 지정:

`ppmtompeg -frames {{첫_프레임}} {{마지막_프레임}} {{경로/대상/매개_변수_파일}}`

- 여러 MPEG 프레임을 단일 MPEG-1 스트림으로 결합:

`ppmtompeg -combine_frames {{경로/대상/매개_변수_파일}}`
