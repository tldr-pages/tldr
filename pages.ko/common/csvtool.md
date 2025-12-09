# csvtool

> CSV 형식의 소스.
> 더 많은 정보: <https://github.com/maroofi/csvtool>.

- CSV 파일에서 두 번째 열을 추출:

`csvtool --column {{2}} {{경로/대상/파일.csv}}`

- CSV 파일에서 두 번째 및 네 번째 열을 추출:

`csvtool --column {{2,4}} {{경로/대상/파일.csv}}`

- 두 번째 열이 'Foo'와 정확히 일치하는 CSV 파일에서 줄을 추출:

`csvtool --column {{2}} --search '{{^Foo$}}' {{경로/대상/파일.csv}}`

- 두 번째 열이 'Bar'로 시작하는 CSV 파일에서 줄을 추출:

`csvtool --column {{2}} --search '{{^Bar}}' {{경로/대상/파일.csv}}`

- 두 번째 열이 'Baz'로 끝나는 CSV 파일의 줄을 찾은 다음, 세 번째와 여섯 번째 열을 추출:

`csvtool --column {{2}} --search '{{Baz$}}' {{경로/대상/파일.csv}} | csvtool --no-header --column {{3,6}}`
