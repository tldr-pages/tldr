# python -m json.tool

> JSON 데이터를 검증하고 보기 좋게 출력.
> Python 표준 라이브러리의 일부.
> 더 많은 정보: <https://docs.python.org/library/json.html#module-json.tool>.

- JSON 파일을 보기 좋게 출력:

`python -m json.tool {{경로/대상/파일.json}}`

- 표준 입력(`stdin`)의 JSON 데이터를 검증하고 보기 좋게 출력:

`echo '{{{"key": "value"}}}' | python -m json.tool`
