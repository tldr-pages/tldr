# pngcheck

> PNG 기반(PNG, JNG, MNG) 이미지 파일의 무결성을 검증하는 포렌식 도구.
> 파일에서 내장된 이미지와 텍스트를 추출할 수도 있습니다.
> 더 많은 정보: <http://www.libpng.org/pub/png/apps/pngcheck.html>.

- 이미지 파일의 무결성 검증:

`pngcheck {{경로/대상/파일.png}}`

- [v]자세히 및 [c]olorized 출력으로 파일 확인:

`pngcheck -vc {{경로/대상/파일.png}}`

- [t]ext 청크 내용 표시 및 특정 파일 내의 PNG 검색:

`pngcheck -ts {{경로/대상/파일.png}}`

- 특정 파일 내에 내장된 PNG 검색 및 e[x]tract 추출:

`pngcheck -x {{경로/대상/파일.png}}`
