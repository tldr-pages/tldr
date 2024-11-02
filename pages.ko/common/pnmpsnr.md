# pnmpsnr

> 두 이미지 간의 차이를 계산.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmpsnr.html>.

- 두 이미지 간의 차이, 즉 최고 신호 대 잡음비(PSNR) 계산:

`pnmpsnr {{경로/대상/파일1.pnm}} {{경로/대상/파일2.pnm}}`

- 이미지의 휘도 및 색도 성분이 아닌 색상 성분을 비교:

`pnmpsnr {{경로/대상/파일1.pnm}} {{경로/대상/파일2.pnm}} -rgb`

- 비교 모드로 실행, 즉 계산된 PSNR이 `n`을 초과하는지 여부에 따라 `nomatch` 또는 `match` 출력:

`pnmpsnr {{경로/대상/파일1.pnm}} {{경로/대상/파일2.pnm}} -target {{n}}`

- 비교 모드로 실행하고 개별 이미지 성분, 즉 Y, Cb 및 Cr을 해당 임계값과 비교:

`pnmpsnr {{경로/대상/파일1.pnm}} {{경로/대상/파일2.pnm}} -target1 {{threshold_Y}} -target2 {{threshold_Cb}} -target3 {{threshold_Cr}}`

- 비교 모드로 실행하고 개별 이미지 성분, 즉 red, green 및 blue를 해당 임계값과 비교:

`pnmpsnr {{경로/대상/파일1.pnm}} {{경로/대상/파일2.pnm}} -rgb -target1 {{threshold_red}} -target2 {{threshold_green}} -target3 {{threshold_blue}}`

- 기계 판독 가능 출력 생성:

`pnmpsnr {{경로/대상/파일1.pnm}} {{경로/대상/파일2.pnm}} -machine`
