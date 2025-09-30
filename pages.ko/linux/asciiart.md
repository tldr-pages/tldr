# asciiart

> 이미지를 ASCII로 변환합니다.
> 더 많은 정보: <https://github.com/nodanaonlyzuul/asciiart>.

- 파일에서 이미지를 읽어와 ASCII로 출력:

`asciiart {{경로/대상/이미지.jpg}}`

- URL에서 이미지를 읽어와 ASCII로 출력:

`asciiart {{www.example.com/image.jpg}}`

- 출력 너비 선택 (기본값은 100):

`asciiart --width {{50}} {{경로/대상/이미지.jpg}}`

- ASCII 출력에 색상 적용:

`asciiart --color {{경로/대상/이미지.jpg}}`

- 출력 형식 선택 (기본 형식은 텍스트):

`asciiart --format {{text|html}} {{경로/대상/이미지.jpg}}`

- 문자 맵을 반전:

`asciiart --invert-chars {{경로/대상/이미지.jpg}}`
