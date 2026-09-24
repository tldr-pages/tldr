# systemctl add-requires

> 하나 이상의 유닛에 대해 특정 타겟에 `Requires` 의존성을 추가.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#add-wants%20TARGET%20UNIT%E2%80%A6>.

- 타겟에서 유닛으로 `Requires` 의존성 추가:

`systemctl add-requires {{타겟}} {{유닛}}`

- 여러 개의 `Requires` 의존성을 한 번에 추가:

`systemctl add-requires {{타겟}} {{유닛1 유닛2 ...}}`

- 사용자 레벨의 `Requires` 의존성 추가:

`systemctl add-requires {{타겟}} {{유닛}} --user`
