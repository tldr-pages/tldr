# ajson

> JSON 객체에서 JSONPath를 실행합니다.
> 더 많은 정보: <https://github.com/spyzhov/ajson>.

- 파일에서 JSON을 읽고 지정된 JSONPath 표현식을 실행:

`ajson '{{$..json[?(@.path)]}}' {{경로/대상/파일.json}}`

- `stdin`에서 JSON을 읽고 지정된 JSONPath 표현식을 실행:

`cat {{경로/대상/파일.json}} | ajson '{{$..json[?(@.path)]}}'`

- URL에서 JSON을 읽고 지정된 JSONPath 표현식을 평가:

`ajson '{{avg($..price)}}' '{{https://example.com/api/}}'`

- 간단한 JSON을 읽고 값을 계산:

`echo '{{3}}' | ajson '{{2 * pi * $}}'`
