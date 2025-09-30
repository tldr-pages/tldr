# einfo

> 각 데이터베이스 필드에 색인된 레코드 수, 데이터베이스의 마지막 업데이트 날짜 및 데이터베이스에서 다른 Entrez 데이터베이스로의 사용 가능한 링크를 제공합니다.
> 더 많은 정보: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- 모든 데이터베이스 이름 출력:

`einfo -dbs`

- 단백질 데이터베이스의 모든 정보를 XML 형식으로 출력:

`einfo -db {{protein}}`

- nuccore 데이터베이스의 모든 필드 출력:

`einfo -db {{nuccore}} -fields`

- 단백질 데이터베이스의 모든 링크 출력:

`einfo -db {{protein}} -links`
