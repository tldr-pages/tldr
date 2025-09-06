# wami

> 작업에 적합한 프로그램을 추천하는 오픈 소스 및 사용하기 쉬운 도구.
> 더 많은 정보: <https://github.com/evait-security/wami>.

- 모든 카테고리에서 결과를 찾아 지정된 순서로 [S]정렬:

`wami --show-all -S {{asc|desc}} --search-all {{검색어}}`

- GitHub에서 확장된 결과를 찾아 내림차순으로 [S]정렬:

`wami --show-all -S desc --github {{검색어}}`

- GitHub에서 검색어와 일치하는 주제 검색:

`wami --list-topics {{검색어}}`

- pentest에 사용되는 도구를 검색하여 기본 자격 증명에 대해 쿼리하고 결과를 내림차순으로 [S]정렬:

`wami -S desc --search-all pentest credential default`
