# keep-header

> 첫 번째 줄을 명령어에 의해 처리하지 않고 그대로 `stdout`에 전달.
> 더 많은 정보: <https://github.com/eBay/tsv-utils#keep-header>.

- 파일을 정렬하고 첫 번째 줄을 맨 위에 유지:

`keep-header {{경로/대상/파일}} -- sort`

- 첫 번째 줄을 `stdout`에 직접 출력하고 파일의 나머지를 지정된 명령어로 처리:

`keep-header {{경로/대상/파일}} -- {{명령어}}`

- `stdin`에서 읽어 첫 번째 줄을 제외한 모든 줄을 정렬:

`cat {{경로/대상/파일}} | keep-header -- {{명령어}}`

- 파일을 `grep`하여 검색 패턴에 상관없이 첫 번째 줄을 유지:

`keep-header {{경로/대상/파일}} -- grep {{패턴}}`
