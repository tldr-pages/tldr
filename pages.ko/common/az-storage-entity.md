# az storage entity

> Azure Table storage 엔티티를 관리.
> `azure-cli`의 일부 (`az`라고도 함).
> 더 많은 정보: <https://learn.microsoft.com/cli/azure/storage/entity>.

- 테이블에 엔터티를 삽입:

`az storage entity insert --entity {{space_separated_key_value_pairs}} --table-name {{테이블_이름}} --account-name {{스토리지_계정_이름}} --account-key {{스토리지_계정_키}}`

- 테이블에서 기존 엔터티를 삭제:

`az storage entity delete --partition-key {{파티션_키}} --row-key {{행_키}} --table-name {{테이블_이름}} --account-name {{스토리지_계정_이름}} --account-key {{스토리지_계정_키}}`

- 해당 속성을 병합하여 기존 엔터티를 업데이트:

`az storage entity merge --entity {{space_separated_key_value_pairs}} --table-name {{테이블_이름}} --account-name {{스토리지_계정_이름}} --account-key {{스토리지_계정_키}}`

- 쿼리를 만족하는 항목을 나열:

`az storage entity query --filter {{쿼리_필터}} --table-name {{테이블_이름}} --account-name {{스토리지_계정_이름}} --account-key {{스토리지_계정_키}}`

- 지정된 테이블에서 엔터티를 가져옴:

`az storage entity show --partition-key {{파티션_키}} --row-key {{행_키}} --table-name {{테이블_이름}} --account-name {{스토리지_계정_이름}} --account-key {{스토리지_계정_키}}`
