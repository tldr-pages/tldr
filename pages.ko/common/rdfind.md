# rdfind

> 중복된 내용을 가진 파일을 찾아 제거.
> 더 많은 정보: <https://rdfind.pauldreik.se/rdfind.1.html>.

- 주어진 디렉터리에서 모든 중복 파일을 식별하고 요약 출력:

`rdfind -dryrun true {{경로/대상/폴더}}`

- 모든 중복 파일을 하드 링크로 교체:

`rdfind -makehardlinks true {{경로/대상/폴더}}`

- 모든 중복 파일을 심볼릭 링크/소프트 링크로 교체:

`rdfind -makesymlinks true {{경로/대상/폴더}}`

- 모든 중복 파일 삭제하고 빈 파일 무시 안 함:

`rdfind -deleteduplicates true -ignoreempty false {{경로/대상/폴더}}`
