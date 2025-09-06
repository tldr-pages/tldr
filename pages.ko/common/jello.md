# jello

> Python 구문을 사용하는 명령줄 JSON 처리기.
> 더 많은 정보: <https://github.com/kellyjonbrazil/jello>.

- `stdin`에서 `stdout`으로 JSON 또는 JSON-Lines 데이터를 보기 좋게 출력:

`cat {{파일.json}} | jello`

- `stdin`에서 `stdout`으로 JSON 또는 JSON Lines 데이터의 스키마 출력 (grep에 유용):

`cat {{파일.json}} | jello -s`

- `stdin`에서 `stdout`으로 JSON 또는 JSON-Lines 데이터의 배열의 모든 요소 (또는 객체의 모든 값) 출력:

`cat {{파일.json}} | jello -l`

- `stdin`에서 `stdout`으로 JSON 또는 JSON-Lines 데이터의 첫 번째 요소 출력:

`cat {{파일.json}} | jello _[0]`

- `stdin`에서 `stdout`으로 JSON 또는 JSON-Lines 데이터의 각 요소에서 주어진 키의 값 출력:

`cat {{파일.json}} | jello '[i.{{키_이름}} for i in _]'`

- (입력 JSON에 `key_name1` 및 `key_name2` 키가 있다고 가정할 때) 여러 키의 값을 새 JSON 객체로 출력:

`cat {{파일.json}} | jello '{"{{키1}}": _.{{key_name1}}, "{{key_name}}": _.{{key_name2}}}'`

- 문자열로 주어진 키의 값 출력 (JSON 출력 비활성화):

`cat {{파일.json}} | jello -r '"{{문자열}}: " + _.{{키_이름}}'`
