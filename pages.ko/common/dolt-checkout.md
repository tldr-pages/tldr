# dolt checkout

> 작업 트리나 테이블을 브랜치나 커밋으로 체크아웃.
> 더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-checkout>.

- 브랜치 교체:

`dolt checkout {{브랜치_이름}}`

- 스테이지되지 않은 변경 사항을 테이블로 되돌림:

`dolt checkout {{테이블}}`

- 새로운 브랜치를 생성하고, 그 브랜치로 체크아웃:

`dolt checkout -b {{브랜치_이름}}`

- 지정된 커밋을 기반으로 새로운 브랜치를 생성하고 해당 커밋으로 전환:

`dolt checkout -b {{브랜치_이름}} {{커밋}}`
