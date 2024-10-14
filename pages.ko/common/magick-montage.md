# magick montage

> 이미지를 사용자 지정 가능한 그리드로 배열.
> 같이 보기: `magick`.
> 더 많은 정보: <https://imagemagick.org/script/montage.php>.

- 이미지를 그리드로 배열하고, 그리드 셀 크기보다 큰 이미지를 자동으로 크기 조정:

`magick montage {{경로/대상/이미지1.jpg 경로/대상/이미지2.jpg ...}} {{경로/대상/몽타주.jpg}}`

- 가장 큰 이미지로부터 그리드 셀 크기를 자동 계산하여 이미지를 그리드로 배열:

`magick montage {{경로/대상/이미지1.jpg 경로/대상/이미지2.jpg ...}} -geometry {{+0+0}} {{경로/대상/몽타주.jpg}}`

- 그리드 셀 크기를 지정하고, 타일링 전에 이미지를 해당 크기에 맞게 조정:

`magick montage {{경로/대상/이미지1.jpg 경로/대상/이미지2.jpg ...}} -geometry {{640x480+0+0}} {{경로/대상/몽타주.jpg}}`

- 그리드의 행과 열 수를 제한하여 입력 이미지가 여러 출력 몽타주로 넘치도록 설정:

`magick montage {{경로/대상/이미지1.jpg 경로/대상/이미지2.jpg ...}} -geometry {{+0+0}} -tile {{2x3}} {{몽타주_%d.jpg}}`

- 타일링 전에 이미지를 그리드 셀에 맞게 크기 조정 및 자르기:

`magick montage {{경로/대상/이미지1.jpg 경로/대상/이미지2.jpg ...}} -geometry {{+0+0}} -resize {{640x480^}} -gravity {{center}} -crop {{640x480+0+0}} {{경로/대상/몽타주.jpg}}`
