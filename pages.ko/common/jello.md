# jello

> Python 구문을 사용하는 명령줄 JSON 처리기.
> 더 많은 정보: <https://github.com/kellyjonbrazil/jello>.

- `stdin`의 JSON 또는 JSON-Lines 데이터를 `stdout`으로 보기 좋게 출력:

`cat {{파일.json}} | jello`

- `stdin`의 JSON 또는 JSON-Lines 데이터의 스키마를 `stdout`으로 출력 (grep에 유용):

`cat {{파일.json}} | jello -s`

- `stdin`의 JSON 또는 JSON-Lines 데이터에서 배열의 모든 요소(또는 객체의 모든 값)를 `stdout`으로 출력:

`cat {{파일.json}} | jello -l`

- `stdin`의 JSON 또는 JSON-Lines 데이터에서 첫 번째 요소를 `stdout`으로 출력:

`cat {{파일.json}} | jello _[0]`

- `stdin`의 JSON 또는 JSON-Lines 데이터에서 각 요소의 주어진 키의 값을 `stdout`으로 출력:

`cat {{파일.json}} | jello '[i.{{키_이름}} for i in _]'`

- 여러 키의 값을 새 JSON 객체로 출력 (입력 JSON에 `key_name1` 및 `key_name2` 키가 있다고 가정):

`cat {{파일.json}} | jello '{"{{키1}}": _.{{키_이름1}}, "{{키_이름}}": _.{{키_이름2}}}'`

- 주어진 키의 값을 문자열로 출력 (JSON 출력 비활성화):

`cat {{파일.json}} | jello -r '"{{일부 텍스트}}: " + _.{{키_이름}}'`
