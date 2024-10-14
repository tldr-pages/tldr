# magick convert

> 이미지 형식 간 변환, 크기 조정, 병합, 생성 등을 수행.
> 참고: 이 도구는 이전의 `convert`로, ImageMagick 7+에서 `magick`으로 대체되었습니다.
> 더 많은 정보: <https://imagemagick.org/script/convert.php>.

- 이미지를 JPEG에서 PNG로 변환:

`magick convert {{경로/대상/입력_이미지.jpg}} {{경로/대상/출력_이미지.png}}`

- 이미지를 원래 크기의 50%로 조정:

`magick convert {{경로/대상/입력_이미지.png}} -resize 50% {{경로/대상/출력_이미지.png}}`

- 이미지의 원본 비율을 유지하며 최대 크기가 640x480이 되도록 축소:

`magick convert {{경로/대상/입력_이미지.png}} -resize 640x480 {{경로/대상/출력_이미지.png}}`

- 지정된 파일 크기를 가지도록 이미지 크기 조정:

`magick convert {{경로/대상/입력_이미지.png}} -define jpeg:extent=512kb {{경로/대상/출력_이미지.jpg}}`

- 이미지를 수직/수평으로 결합:

`magick convert {{경로/대상/이미지1.png 경로/대상/이미지2.png ...}} {{-append|+append}} {{경로/대상/출력_이미지.png}}`

- 100ms 간격의 이미지 시리즈로 GIF 생성:

`magick convert {{경로/대상/이미지1.png 경로/대상/이미지2.png ...}} -delay {{10}} {{경로/대상/애니메이션.gif}}`

- 단색 빨간색 배경만 있는 이미지 생성:

`magick convert -size {{800x600}} "xc:{{#ff0000}}" {{경로/대상/이미지.png}}`

- 여러 크기의 이미지를 사용하여 파비콘 생성:

`magick convert {{경로/대상/이미지1.png 경로/대상/이미지2.png ...}} {{경로/대상/favicon.ico}}`
