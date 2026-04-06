# systemctl cancel

> 시스템 매니저 또는 사용자 매니저에서 대기 중인 하나 이상의 작업을 취소.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#cancel%20JOB%E2%80%A6>.

- 숫자 ID로 작업 취소:

`systemctl cancel {{작업_id}}`

- 여러 작업을 한 번에 취소:

`systemctl cancel {{작업_id1 작업_id2 ...}}`

- 모든 대기 중인 작업 취소:

`systemctl cancel`

- 사용자 서비스 매니저에서 작업 취소:

`systemctl cancel {{작업_id}} --user`
