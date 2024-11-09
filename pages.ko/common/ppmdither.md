# ppmdither

> 디더링을 적용하여 이미지의 색상 수를 줄입니다.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmdither.html>.

- PPM 이미지를 읽고 디더링을 적용하여 파일로 저장:

`ppmdither {{경로/대상/이미지.ppm}} > {{경로/대상/파일.ppm}}`

- 각 기본 색상에 대한 원하는 음영 수 지정:

`ppmdither -red {{2}} -green {{3}} -blue {{2}} {{경로/대상/이미지.ppm}} > {{경로/대상/파일.ppm}}`

- 디더링 행렬의 크기 지정:

`ppmdither -dim {{2}} {{경로/대상/이미지.ppm}} > {{경로/대상/파일.ppm}}`
