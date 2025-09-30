# exif

> JPEG 파일의 EXIF 정보를 표시하고 변경.
> 더 많은 정보: <https://manned.org/exif>.

- 이미지에서 인식된 모든 EXIF 정보 표시:

`exif {{경로/대상/이미지.jpg}}`

- 이미지에 존재하는지 여부와 함께 알려진 EXIF 태그 목록을 표로 표시:

`exif --list-tags --no-fixup {{이미지.jpg}}`

- 이미지 썸네일을 `thumbnail.jpg` 파일로 추출:

`exif --extract-thumbnail --output={{thumbnail.jpg}} {{이미지.jpg}}`

- 주어진 이미지에서 "Model" 태그의 원시 내용 표시:

`exif --ifd={{0}} --tag={{Model}} --machine-readable {{이미지.jpg}}`

- "Artist" 태그의 값을 John Smith로 변경하고 `new.jpg`로 저장:

`exif --output={{new.jpg}} --ifd={{0}} --tag="{{Artist}}" --set-value="{{John Smith}}" --no-fixup {{이미지.jpg}}`
