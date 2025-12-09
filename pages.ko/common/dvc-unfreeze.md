# dvc unfreeze

> DVC 파이프라인에서 스테이지의 동결을 해제.
> 이는 동결된 후 스테이지의 의존성 변경 사항을 DVC가 다시 추적할 수 있게 합니다.
> 같이 보기: `dvc freeze`.
> 더 많은 정보: <https://dvc.org/doc/command-reference/unfreeze>.

- 하나 이상의 지정된 스테이지 동결 해제:

`dvc unfreeze {{스테이지_이름1 스테이지_이름2 ...}}`
