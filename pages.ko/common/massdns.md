# massdns

> 대규모 DNS 레코드 조회를 정찰 용도로 고성능으로 수행하는 도구.
> 관련 항목: `dig`, `dnsx`.
> 더 많은 정보: <https://github.com/blechschmidt/massdns#usage>.

- 지정한 DNS Resolver를 사용하여 파일에 있는 도메인의 `A` 레코드를 조회 :

`massdns {{[-r|--resolvers]}} {{경로/대상/resolvers.txt}} {{경로/대상/도메인.txt}}`

- 특정 레코드 타입을 조회하고 결과를 파일에 저장:

`massdns {{[-r|--resolvers]}} {{경로/대상/resolvers.txt}} {{[-t|--type]}} {{A|AAAA|NS|MX|TXT}} {{[-w|--outfile]}} {{경로/대상/출력파일.txt}} {{경로/대상/도메인.txt}}`

- 도메인을 조회하고 단순 텍스트 형식으로 출력:

`massdns {{[-r|--resolvers]}} {{경로/대상/resolvers.txt}} {{[-o|--output]}} S {{경로/대상/도메인.txt}}`

- 도메인을 조회하고 JSON 형식으로 출력 :

`massdns {{[-r|--resolvers]}} {{경로/대상/resolvers.txt}} {{[-o|--output]}} J {{경로/대상/도메인.txt}}`

- 사용자 지정 동시 조회 수로 도메인을 조회 :

`massdns {{[-r|--resolvers]}} {{경로/대상/resolvers.txt}} {{[-s|--hashmap-size]}} {{10000}} {{경로/대상/도메인.txt}}`

- 상태 출력 없는 조용한 모드로 조회:

`massdns {{[-r|--resolvers]}} {{경로/대상/resolvers.txt}} {{[-q|--quiet]}} {{경로/대상/도메인.txt}}`
