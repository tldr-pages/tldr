# dolt merge

> 두 개 이상의 개발 이력을 함께 결합.
> 더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-merge>.

- 지정된 커밋의 변경 사항을 현재 브랜치에 통합:

`dolt merge {{브랜치_이름}}`

- 지정된 커밋의 변경 사항을 커밋 기록을 업데이트하지 않고 현재 브랜치에 통합:

`dolt merge --squash {{브랜치_이름}}`

- 브랜치를 병합하고, 병합이 빠른 병합(FF)으로 해결되더라도 병합 커밋 생성:

`dolt merge --no-ff {{브랜치_이름}}`

- 특정 커밋 메시지와 함께 브랜치를 병합하고 병합 커밋 생성:

`dolt merge --no-ff -m "{{메시지}}" {{브랜치_이름}}`

- 현재 충돌 해결 프로세스 중단:

`dolt merge --abort`
