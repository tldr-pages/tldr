# ppmforge

> 구름, 행성 및 별이 빛나는 하늘과 같은 프랙탈을 생성합니다.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmforge.html>.

- 행성 이미지를 생성:

`ppmforge > {{경로/대상/이미지.ppm}}`

- 구름이나 밤하늘 이미지를 생성:

`ppmforge -{{night|clouds}} > {{경로/대상/이미지.ppm}}`

- 프랙탈 생성에 사용자 정의 메쉬 크기와 차원을 사용하고 출력의 크기를 지정:

`ppmforge -mesh {{512}} -dimension {{2.5}} -xsize {{1000}} -ysize {{1000}} > {{경로/대상/이미지.ppm}}`

- 생성된 행성의 기울기 및 조명 각도 조절:

`ppmforge -tilt {{-15}} -hour {{12}} > {{경로/대상/이미지.ppm}}`
