# dolt merge

> 두 개 이상의 개발 이력을 함께 결합.
> 더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-merge>.

- 이름이 있는 커밋의 변경 사항을 현재 브랜치에 통합:

`dolt merge {{브랜치_이름}}`

- 커밋 기록을 업데이트하지 않고, 명명된 커밋의 변경 사항을 현재 브랜치에 통합:

`dolt merge --squash {{브랜치_이름}}`

- 병합이 빨리-감기로 해결되는 경우에도, 브랜치를 병합하고 병합 커밋을 생성:

`dolt merge --no-ff {{브랜치_이름}}`

- 브랜치를 병합하고 특정 커밋 메시지가 포함된 병합 커밋을 생성:

`dolt merge --no-ff -m "{{메시지}}" {{브랜치_이름}}`

- 현재 충돌 해결 프로세스를 중단:

`dolt merge --abort`
