# dvc freeze

> DVC 파이프라인의 스테이지를 동결.
> 이는 스테이지 종속성의 변경 사항을 추적하고, 해동될 때까지 재실행을 방지합니다.
> 같이 보기: `dvc unfreeze`.
> 더 많은 정보: <https://dvc.org/doc/command-reference/freeze>.

- 하나 이상의 특정 스테이지를 동결:

`dvc freeze {{스테이지_이름1 스테이지_이름2 ...}}`
