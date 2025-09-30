# mdfind

> 쿼리에 맞는 파일 나열.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/mdfind.1.html>.

- 파일 이름으로 찾기:

`mdfind -name {{파일}}`

- 파일 내용을 통해 찾기:

`mdfind "{{쿼리}}"`

- 특정 디렉토리 내 문자열을 포함하는 파일 찾기:

`mdfind -onlyin {{경로/대상/폴더}} "{{쿼리}}"`
