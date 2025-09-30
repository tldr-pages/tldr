# ppmshadow

> PPM 이미지에 시뮬레이션된 그림자를 추가.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmshadow.html>.

- PPM 이미지에 시뮬레이션된 그림자 추가:

`ppmshadow {{경로/대상/입력_파일.ppm}} > {{경로/대상/출력_파일.ppm}}`

- 이미지를 지정된 픽셀 수만큼 [b]블러 처리:

`ppmshadow -b {{n}} {{경로/대상/입력_파일.ppm}} > {{경로/대상/출력_파일.ppm}}`

- 이미지의 왼쪽과 위쪽으로 시뮬레이션된 광원의 변위를 지정:

`ppmshadow -x {{왼쪽_오프셋}} -y {{위쪽_오프셋}} {{경로/대상/입력_파일.ppm}} > {{경로/대상/출력_파일.ppm}}`
