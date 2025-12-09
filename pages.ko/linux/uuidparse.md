# uuidparse

> 범용 고유 식별자(UUID) 파싱.
> 같이 보기: `uuidgen`.
> 더 많은 정보: <https://manned.org/uuidparse.1>.

- 지정된 UUID를 파싱하고 표 형식으로 출력:

`uuidparse {{uuid1 uuid2 ...}}`

- `stdin`에서 UUID 파싱:

`{{명령어}} | uuidparse`

- JSON 출력 형식 사용:

`uuidparse --json {{uuid1 uuid2 ...}}`

- 헤더 줄을 출력하지 않음:

`uuidparse --noheadings {{uuid1 uuid2 ...}}`

- 원시 출력 형식 사용:

`uuidparse --raw {{uuid1 uuid2 ...}}`

- 출력할 네 가지 열을 지정:

`uuidparse --output {{UUID,VARIANT,TYPE,TIME}}`

- 도움말 표시:

`uuidparse -h`
