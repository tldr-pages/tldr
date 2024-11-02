# pngcheck

> PNG, JNG 및 MNG 파일에 대한 자세한 정보를 출력하고 파일을 검증합니다.
> 더 많은 정보: <http://www.libpng.org/pub/png/apps/pngcheck.html>.

- 이미지 요약 정보 출력 (너비, 높이 및 색상 깊이):

`pngcheck {{경로/대상/이미지.png}}`

- [c]olorized 출력으로 이미지 정보 출력:

`pngcheck -c {{경로/대상/이미지.png}}`

- 이미지에 대한 [v]erbose 정보 출력:

`pngcheck -cvt {{경로/대상/이미지.png}}`

- `stdin`에서 이미지를 받아 상세 정보 출력:

`cat {{경로/대상/이미지.png}} | pngcheck -cvt`

- 특정 파일 내에서 PNG 검색하고 정보 표시:

`pngcheck -s {{경로/대상/이미지.png}}`

- 다른 파일 내에서 PNG 검색하고 추출 [e]xtract:

`pngcheck -x {{경로/대상/이미지.png}}`
