# peludna-prognoza

> Pliva의 알레르기 데이터 API를 사용하여 터미널에서 크로아티아 도시의 꽃가루 측정 데이터를 가져옵니다.
> 더 많은 정보: <https://github.com/vladimyr/peludna-prognoza>.

- 도시를 대화형으로 검색하고 데이터를 가져오기:

`peludna-prognoza`

- 특정 도시의 데이터 가져오기:

`peludna-prognoza "{{도시}}"`

- 기계 판독 가능한 형식으로 데이터 표시:

`peludna-prognoza "{{도시}}" --{{json|xml}}`

- 기본 웹 브라우저에서 <https://plivazdravlje.hr>의 특정 도시 꽃가루 측정 페이지 표시:

`peludna-prognoza "{{도시}}" --web`
