# magick

> 이미지 형식 간 변환, 편집, 합성 또는 변환.
> 이 도구는 ImageMagick 7+에서 `convert`를 대체합니다. 7+ 버전에서 이전 도구를 사용하려면 `magick convert`를 참조하세요.
> `mogrify`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://imagemagick.org>.

- 이미지 형식 간 변환:

`magick {{경로/대상/입력_이미지.png}} {{경로/대상/출력_이미지.jpg}}`

- 이미지를 크기 조정하여 새 복사본 만들기:

`magick {{경로/대상/입력_이미지.jpg}} -resize {{100x100}} {{경로/대상/출력_이미지.jpg}}`

- 현재 디렉토리의 모든 JPEG 이미지로 GIF 생성:

`magick {{*.jpg}} {{경로/대상/이미지.gif}}`

- 체커보드 패턴 생성:

`magick -size {{640x480}} pattern:checkerboard {{경로/대상/체커보드.png}}`

- 현재 디렉토리의 모든 JPEG 이미지로 PDF 파일 생성:

`magick {{*.jpg}} -adjoin {{경로/대상/파일.pdf}}`
