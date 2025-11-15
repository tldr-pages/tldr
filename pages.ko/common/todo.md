# todo

> 간단하고 표준 기반의 CLI 할 일 관리 도구.
> 더 많은 정보: <https://todoman.readthedocs.io>.

- 시작할 수 있는 작업 목록:

`todo list --startable`

- 작업 목록에 새 작업 추가:

`todo new {{할_일}} --list {{작업_목록}}`

- 지정된 ID의 작업에 위치 추가:

`todo edit --location {{위치_이름}} {{작업_ID}}`

- 작업에 대한 세부 정보 표시:

`todo show {{작업_ID}}`

- 지정된 ID의 작업 완료로 표시:

`todo done {{작업_ID1 작업_ID2 ...}}`

- 작업 삭제:

`todo delete {{작업_ID}}`

- 완료된 작업 삭제 및 남은 작업 ID 초기화:

`todo flush`
