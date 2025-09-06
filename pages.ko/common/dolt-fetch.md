# dolt fetch

> 다른 저장소에서 객체와 참조를 다운로드.
> 더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-fetch>.

- 기본 원격 업스트림 저장소(origin)에서 최신 변경 사항을 가져옴:

`dolt fetch`

- 특정 원격 업스트림 저장소에서 최신 변경 사항을 가져옴:

`dolt fetch {{원격_이름}}`

- 원격의 현재 상태로 브랜치를 업데이트하고, 충돌하는 기록을 덮어씀:

`dolt fetch -f`
