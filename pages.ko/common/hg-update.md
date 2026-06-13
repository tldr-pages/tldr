# hg update

> 작업 디렉터리를 지정된 변경 집합으로 업데이트.
> 더 많은 정보: <https://www.mercurial-scm.org/help/commands/update>.

- 현재 브랜치의 최신 변경 사항으로 업데이트:

`hg update`

- 지정된 리비전으로 업데이트:

`hg update {{[-r|--rev]}} {{리비전}}`

- 커밋되지 않은 변경 사항을 폐기하고 업데이트:

`hg update {{[-C|--clean]}}`

- 지정된 날짜와 일치하는 마지막 커밋으로 업데이트:

`hg update {{[-d|--date]}} {{일-월-연도}}`
