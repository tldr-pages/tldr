# systemctl freeze

> 하나 이상의 유닛을 일시 정지 상태로 만듬.
> 정지된 유닛은 `systemctl thaw`로 다시 실행 가능.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#freeze%20PATTERN%E2%80%A6>.

- 특정 유닛 일시 정지:

`systemctl freeze {{유닛}}`

- 여러 유닛 일시 정지:

`systemctl freeze {{유닛1 유닛2 ...}}`

- 실행 중인 모든 유닛 일시 정지:

`systemctl freeze '*'`
