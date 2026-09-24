# systemctl restart

> 하나 이상의 systemd 유닛을 중지한 후 다시 시작.
> 중지된 유닛에는 `systemctl start` 대신 사용할 수 있지만, 실행 중인 유닛이 실수로 재시작되는 것을 방지하려면 `start`를 사용하는 것이 더 안전.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#restart%20PATTERN%E2%80%A6>.

- 유닛 재시작:

`systemctl restart {{유닛}}`

- 여러 유닛 재시작:

`systemctl restart {{유닛1 유닛2 ...}}`

- 사용자 유닛 재시작:

`systemctl restart {{유닛}} --user`
