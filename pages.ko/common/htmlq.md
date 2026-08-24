# htmlq

> CSS 선택자를 사용하여 HTML 파일에서 원하는 내용을 추출하는 도구.
> 더 많은 정보: <https://github.com/mgdm/htmlq#usage>.

- `card` 클래스의 모든 요소 반환:

`cat {{경로/대상/파일.html}} | htmlq '.card'`

- 첫 번째 p 요소의 텍스트 내용 가져오기:

`cat {{경로/대상/파일.html}} | htmlq {{[-t|--text]}} 'p:first-of-type'`

- 페이지 내 모든 링크 추출:

`cat {{경로/대상/파일.html}} | htmlq {{[-a|--attribute]}} href 'a'`

- 페이지에서 모든 이미지와 SVG 제거:

`cat {{경로/대상/파일.html}} | htmlq {{[-r|--remove-nodes]}} 'img' {{[-r|--remove-nodes]}} 'svg'`

- 보기 좋게 포맷하여 파일로 출력:

`htmlq {{[-p|--pretty]}} {{[-f|--filename]}} {{경로/대상/입력파일.html}} {{[-o|--output]}} {{경로/대상/출력파일.html}}`
