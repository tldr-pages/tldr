# jq

> 도메인 특화 언어(DSL)를 사용하는 JSON 처리기.
> 더 많은 정보: <https://jqlang.github.io/jq/manual/>.

- 특정 표현식을 실행하여 JSON을 색상 및 포맷된 출력으로 표시:

`{{cat 경로/대상/파일.json}} | jq '.'`

- `jq` 바이너리를 사용하여 특정 표현식을 실행하고 JSON을 색상 및 포맷된 출력으로 표시:

`jq '.' {{/경로/대상/파일.json}}`

- 특정 스크립트를 실행:

`{{cat 경로/대상/파일.json}} | jq --from-file {{경로/대상/스크립트.jq}}`

- 특정 인수 전달:

`{{cat 경로/대상/파일.json}} | jq {{--arg "name1" "value1" --arg "name2" "value2" ...}} '{{. + $ARGS.named}}'`

- 특정 키 출력:

`{{cat 경로/대상/파일.json}} | jq '{{.key1, .key2, ...}}'`

- 특정 배열 항목 출력:

`{{cat 경로/대상/파일.json}} | jq '{{.[index1], .[index2], ...}}'`

- 모든 배열/객체 값 출력:

`{{cat 경로/대상/파일.json}} | jq '.[]'`

- 특정 키 추가/제거:

`{{cat 경로/대상/파일.json}} | jq '. {{+|-}} {{{"key1": "value1", "key2": "value2", ...}}}'`
