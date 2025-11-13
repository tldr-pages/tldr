# pngcheck

> PNG, JNG, MNG 파일에 대한 자세한 정보를 출력하고 검증합니다.
> 더 많은 정보: <https://manned.org/pngcheck>.

- 이미지의 요약 정보 출력 (너비, 높이, 색상 깊이):

`pngcheck {{경로/대상/이미지.png}}`

- [c]색상화된 출력으로 이미지 정보 출력:

`pngcheck -c {{경로/대상/이미지.png}}`

- 이미지에 대한 [v]erbose 정보 출력:

`pngcheck -cvt {{경로/대상/이미지.png}}`

- `stdin`에서 이미지를 받아와 자세한 정보 출력:

`cat {{경로/대상/이미지.png}} | pngcheck -cvt`

- 특정 파일 내에서 PNG를 [s]검색하여 정보 출력:

`pngcheck -s {{경로/대상/이미지.png}}`

- 다른 파일 내에서 PNG를 검색하고 [x]추출:

`pngcheck -x {{경로/대상/이미지.png}}`
