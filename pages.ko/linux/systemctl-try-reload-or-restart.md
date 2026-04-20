# systemctl try-reload-or-restart

> 하나 이상의 유닛이 재로드를 지원하면, 재로드하고, 그렇지 않으면 재시작.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#try-reload-or-restart%20PATTERN%E2%80%A6>.

- 특정 유닛 재로드 또는 재시작:

`systemctl try-reload-or-restart {{유닛}}`

- 여러 유닛 재로드 또는 재시작:

`systemctl try-reload-or-restart {{유닛1 유닛2 ...}}`

- 패턴과 일치하는 모든 유닛 재로드 또는 재시작:

`systemctl try-reload-or-restart '{{패턴}}'`
