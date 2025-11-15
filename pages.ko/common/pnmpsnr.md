# pnmpsnr

> 두 이미지 간의 차이를 계산합니다.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmpsnr.html>.

- 두 이미지 간의 차이, 즉 피크 신호 대 잡음비(PSNR) 계산:

`pnmpsnr {{경로/대상/파일1.pnm}} {{경로/대상/파일2.pnm}}`

- 이미지의 휘도 및 색도 성분 대신 색상 성분을 비교:

`pnmpsnr {{경로/대상/파일1.pnm}} {{경로/대상/파일2.pnm}} -rgb`

- 비교 모드로 실행하여, 계산된 PSNR이 `n`을 초과하는지에 따라 `nomatch` 또는 `match`만 출력:

`pnmpsnr {{경로/대상/파일1.pnm}} {{경로/대상/파일2.pnm}} -target {{n}}`

- 비교 모드로 실행하고 개별 이미지 성분, 즉 Y, Cb 및 Cr을 해당 임계값과 비교:

`pnmpsnr {{경로/대상/파일1.pnm}} {{경로/대상/파일2.pnm}} -target1 {{임계값_Y}} -target2 {{임계값_Cb}} -target3 {{임계값_Cr}}`

- 비교 모드로 실행하고 개별 이미지 성분, 즉 빨강, 초록, 파랑을 해당 임계값과 비교:

`pnmpsnr {{경로/대상/파일1.pnm}} {{경로/대상/파일2.pnm}} -rgb -target1 {{임계값_빨강}} -target2 {{임계값_초록}} -target3 {{임계값_파랑}}`

- 기계가 읽을 수 있는 출력 생성:

`pnmpsnr {{경로/대상/파일1.pnm}} {{경로/대상/파일2.pnm}} -machine`
