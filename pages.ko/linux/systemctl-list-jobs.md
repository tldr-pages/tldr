# systemctl list-jobs

> 현재 시스템에서 대기 중이거나 실행 중인 systemd 작업 목록을 표시.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-jobs%20PATTERN%E2%80%A6>.

- 모든 활성 작업 목록 출력:

`systemctl list-jobs`

- 특정 유닛에 대한 작업만 필터링하여 출력:

`systemctl list-jobs {{유닛}}`
