# magick

> 이미지 생성, 편집, 합성 및 포맷 변환.
> ImageMagick 7 이상에서 `convert`를 대체하는 명령어. 7 버전 이상에서 기존 도구를 사용하려면 `magick convert`를 참고.
> 일부 하위 명령어(`mogrify` 등)은 별도의 문서를 제공.
> 더 많은 정보: <https://imagemagick.org/script/magick.php>.

- 이미지 포맷 변환:

`magick {{경로/대상/입력_이미지.png}} {{경로/대상/출력_이미지.jpg}}`

- 이미지 크기 조정 후 새로운 파일 생성:

`magick {{경로/대상/입력_이미지.jpg}} -resize {{100x100}} {{경로/대상/출력_이미지.jpg}}`

- 비율 기준으로 이미지 크기 조정:

`magick {{경로/대상/입력_이미지.png}} -resize {{50}}% {{경로/대상/출력_이미지.png}}`

- 지정한 파일 크기에 맞춰 JPEG 이미지 생성:

`magick {{경로/대상/입력_이미지.png}} -define jpeg:extent={{512kb}} {{경로/대상/출력_이미지.jpg}}`

- 현재 디렉터리의 JPEG 파일들로 GIF 생성:

`magick {{*.jpg}} {{경로/대상/이미지.gif}}`

- 체커보드(Checkerboard) 패턴 이미지 생성:

`magick -size {{640x480}} pattern:checkerboard {{경로/대상/체커보드.png}}`

- 현재 디렉터리의 JPEG 파일들을 PDF로 변환:

`magick {{*.jpg}} -adjoin {{경로/대상/파일.pdf}}`
