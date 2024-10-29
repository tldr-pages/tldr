# dolt checkout

> 작업 트리 또는 테이블을 브랜치 또는 커밋으로 체크아웃.
> 더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-checkout>.

- 브랜치로 전환:

`dolt checkout {{브랜치_이름}}`

- 테이블의 스테이지되지 않은 변경 사항 되돌리기:

`dolt checkout {{테이블}}`

- 새 브랜치를 생성하고 전환:

`dolt checkout -b {{브랜치_이름}}`

- 지정된 커밋을 기반으로 새 브랜치를 생성하고 전환:

`dolt checkout -b {{브랜치_이름}} {{커밋}}`
