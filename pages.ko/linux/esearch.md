# esearch

> 색인된 필드의 용어를 사용하여 새로운 Entrez 검색을 수행합니다.
> `edirect` 패키지의 일부입니다.
> 더 많은 정보: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- pubmed 데이터베이스에서 선택적 세로토닌 재흡수 억제제를 검색:

`esearch -db pubmed -query "{{selective serotonin reuptake inhibitor}}"`

- 쿼리와 정규 표현식을 사용하여 protein 데이터베이스 검색:

`esearch -db {{protein}} -query {{'Escherichia*'}}`

- nuccore 데이터베이스에서 메타데이터에 인슐린과 설치류가 포함된 서열 검색:

`esearch -db nuccore -query "{{insulin [PROT] AND rodents [ORGN]}}"`

- [h]도움말 표시:

`esearch -h`
