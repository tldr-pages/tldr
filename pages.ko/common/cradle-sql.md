# cradle sql

> Cradle SQL 데이터베이스 관리.
> 더 많은 정보: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#sql>.

- 데이터베이스 스키마 재구축:

`cradle sql build`

- 특정 패키지에 대한 데이터베이스 스키마 재구축:

`cradle sql build {{패키지_명}}`

- 전체 데이터베이스 비우기:

`cradle sql flush`

- 특정 패키지에 대한 데이터베이스 테이블 비우기:

`cradle sql flush {{패키지_명}}`

- 모든 패키지에 대한 테이블 채우기:

`cradle sql populate`

- 특정 패키지에 대한 테이블 채우기:

`cradle sql populate {{패키지_명}}`
