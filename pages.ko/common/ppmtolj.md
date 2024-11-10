# ppmtolj

> PPM 파일을 HP LaserJet PCL 5 Color 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtolj.html>.

- PPM 파일을 HP LaserJet PCL 5 Color 파일로 변환:

`ppmtolj {{경로/대상/입력.ppm}} > {{경로/대상/출력.lj}}`

- 지정된 감마 값을 사용하여 감마 보정 적용:

`ppmtolj -gamma {{감마}} {{경로/대상/입력.ppm}} > {{경로/대상/출력.lj}}`

- 필요한 해상도 지정:

`ppmtolj -resolution {{75|100|150|300|600}} {{경로/대상/입력.ppm}} > {{경로/대상/출력.lj}}`
