# ag

> The Silver Searcher. `ack`과 비슷하지만, 더 빠르다.
> 더 많은 정보: <https://manned.org/ag>.

- `string`을 포함하는 파일을 찾고, 일치하는 줄을 주변 문맥과 함께 출력:

`ag string`

- 특정 디렉터리에서 `string`을 포함하는 파일을 찾음:

`ag string {{경로/대상/디렉터리}}`

- `string`을 포함하는 파일을 찾지만, 파일 이름만 출력:

`ag {{[-l|--files-with-matches]}} string`

- 대소문자를 구분하지 않고 `STRING`을 찾고, 줄 전체가 아닌 일치한 부분만 출력:

`ag {{[-i|--ignore-case]}} {{[-o|--only-matching]}} STRING`

- 이름이 `file_name`과 일치하는 파일에서 `string`을 찾음:

`ag string {{[-G|--file-search-regex]}} file_name`

- 내용이 `regex`와 일치하는 파일을 찾음:

`ag '{{^ca(t|r)$}}'`

- 파일 이름이 `string`과 일치하는 파일을 찾음:

`ag {{[-g|--filename-pattern]}} string`
