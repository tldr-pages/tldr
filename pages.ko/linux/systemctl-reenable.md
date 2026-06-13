# systemctl reenable

> 하나 이상의 유닛을 다시 활성화.
> 서비스의 타겟이 변경되었을 때 사용됨.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#reenable%20UNIT%E2%80%A6>.

- 유닛을 재활성화하여, 기본 심볼릭 링크를 복원:

`systemctl reenable {{유닛}}`

- 여러 유닛을 한 번에 재활성화:

`systemctl reenable {{유닛1 유닛2 ...}}`

- 유닛을 재활성화하고 즉시 시작:

`systemctl reenable {{유닛}} --now`
