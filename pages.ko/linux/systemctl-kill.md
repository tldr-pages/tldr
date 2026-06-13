# systemctl kill

> 유닛에 속한 하나 이상의 프로세스에 시그널을 전송.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#kill%20PATTERN%E2%80%A6>.

- 유닛을 종료하기 위해 `SIGTERM` 시그널 전송:

`systemctl kill {{유닛}}`

- 특정 시그널을 유닛에 전송:

`systemctl kill {{[-s|--signal]}} {{시그널_번호|시그널_이름}} {{유닛}}`

- 유닛 메인 프로세스에만 `SIGHUP` 시그널 전송:

`systemctl kill {{[-s|--signal]}} SIGHUP --kill-whom main {{유닛}}`

- 사용 가능한 모든 시그널 목록 출력:

`systemctl kill {{[-s|--signal]}} help`
