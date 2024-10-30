# magick compare

> 두 이미지 간의 차이를 시각적으로 주석 처리하기 위한 비교 이미지를 생성.
> 같이 보기: `magick`.
> 더 많은 정보: <https://imagemagick.org/script/compare.php>.

- 두 이미지 비교:

`magick compare {{경로/대상/이미지1.png}} {{경로/대상/이미지2.png}} {{경로/대상/diff.png}}`

- 지정된 측정 기준을 사용하여 두 이미지 비교:

`magick compare -verbose -metric {{PSNR}} {{경로/대상/image1.png}} {{경로/대상/image2.png}} {{경로/대상/diff.png}}`
