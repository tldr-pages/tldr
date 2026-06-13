# nokogiri

> HTML, XML, SAX 및 Reader 파서.
> 더 많은 정보: <https://manned.org/nokogiri>.

- URL 또는 파일의 내용을 파싱:

`nokogiri {{url|경로/대상/파일}}`

- 특정 타입으로 파싱:

`nokogiri {{url|경로/대상/파일}} --type {{xml|html}}`

- 파싱 전에 특정 초기화 파일 로드:

`nokogiri {{url|경로/대상/파일}} -C {{경로/대상/설정_파일}}`

- 특정 인코딩을 사용하여 파싱:

`nokogiri {{url|경로/대상/파일}} {{[-E|--encoding]}} {{인코딩}}`

- RELAX NG 파일을 사용하여 검증:

`nokogiri {{url|경로/대상/파일}} --rng {{url|경로/대상/파일}}`
