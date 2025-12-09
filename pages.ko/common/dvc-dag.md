# dvc dag

> `dvc.yaml`에 정의된 파이프라인을 시각화.
> 더 많은 정보: <https://dvc.org/doc/command-reference/dag>.

- 전체 파이프라인 시각화:

`dvc dag`

- 지정된 대상 스테이지까지의 파이프라인 스테이지 시각화:

`dvc dag {{대상}}`

- 파이프라인을 dot 형식으로 내보내기:

`dvc dag --dot > {{경로/대상/파이프라인.dot}}`
