# postcss

> JS 플러그인으로 스타일 변환.
> 더 많은 정보: <https://github.com/postcss/postcss-cli#usage>.

- CSS 파일을 파싱하고 변환:

`postcss {{경로/대상/파일}}`

- CSS 파일을 파싱하고 변환하여 특정 파일로 출력:

`postcss {{경로/대상/파일}} --output {{경로/대상/파일}}`

- CSS 파일을 파싱하고 변환하여 특정 폴더에 출력:

`postcss {{경로/대상/파일}} --dir {{경로/대상/폴더}}`

- CSS 파일을 제자리에 파싱하고 변환:

`postcss {{경로/대상/파일}} --replace`

- 사용자 지정 PostCSS 파서를 지정:

`postcss {{경로/대상/파일}} --parser {{파서}}`

- 사용자 지정 PostCSS 구문을 지정:

`postcss {{경로/대상/파일}} --syntax {{구문}}`

- CSS 파일의 변경 사항 감시:

`postcss {{경로/대상/파일}} --watch`

- 도움말 표시:

`postcss --help`
