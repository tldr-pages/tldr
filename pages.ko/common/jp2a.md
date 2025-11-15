# jp2a

> JPEG 이미지를 ASCII로 변환.
> 더 많은 정보: <https://manned.org/jp2a>.

- 파일에서 JPEG 이미지를 읽어 ASCII로 출력:

`jp2a {{경로/대상/이미지.jpeg}}`

- URL에서 JPEG 이미지를 읽어 ASCII로 출력:

`jp2a {{www.example.com/image.jpeg}}`

- ASCII 출력을 색상화:

`jp2a --colors {{경로/대상/이미지.jpeg}}`

- ASCII 출력에 사용할 문자 지정:

`jp2a --chars='{{..-ooxx@@}}' {{경로/대상/이미지.jpeg}}`

- ASCII 출력을 파일에 작성:

`jp2a --output={{경로/대상/출력_파일.txt}} {{경로/대상/이미지.jpeg}}`

- 웹 브라우저에서 볼 수 있도록 HTML 파일 형식으로 ASCII 출력 작성:

`jp2a --html --output={{경로/대상/출력_파일.html}} {{경로/대상/이미지.jpeg}}`
