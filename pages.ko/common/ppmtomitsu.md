# ppmtomitsu

> PPM 이미지를 Mitsubishi S340-10 파일로 변환.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtomitsu.html>.

- PPM 이미지를 MITSU 파일로 변환:

`ppmtomitsu {{경로/대상/파일.ppm}} > {{경로/대상/파일.mitsu}}`

- 이미지를 지정된 배율로 확대하고, 지정된 선명도를 사용하여 `n`개의 복사본 생성:

`ppmtomitsu -enlarge {{1|2|3}} -sharpness {{1|2|3|4}} -copy {{n}} {{경로/대상/파일.ppm}} > {{경로/대상/파일.mitsu}}`

- 인쇄 과정에 주어진 매체 사용:

`ppmtomitsu -media {{A|A4|AS|A4S}} {{경로/대상/파일.ppm}} > {{경로/대상/파일.mitsu}}`
