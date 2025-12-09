# tesseract

> OCR (Optical Character Recognition) 엔진.
> 더 많은 정보: <https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc>.

- 이미지에서 텍스트를 인식하여 `output.txt`에 저장 (`.txt` 확장자는 자동으로 추가됨):

`tesseract {{이미지.png}} {{출력}}`

- ISO 639-2 코드로 사용자 정의 언어 지정 (기본값은 영어, 예: deu = Deutsch = 독일어):

`tesseract -l deu {{이미지.png}} {{출력}}`

- 사용 가능한 언어의 ISO 639-2 코드 나열:

`tesseract --list-langs`

- 사용자 정의 페이지 세분화 모드 지정 (기본값은 3):

`tesseract --psm {{0에서_10}} {{이미지.png}} {{출력}}`

- 페이지 세분화 모드 및 설명 나열:

`tesseract --help-psm`
