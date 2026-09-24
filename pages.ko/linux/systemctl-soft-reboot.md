# systemctl soft-reboot

> 커널은 유지한 채 userspace만 종료 후 재시작하는 소프트 재부팅을 수행.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#soft-reboot>.

- 즉시 소프트 재부팅 실행:

`systemctl soft-reboot`

- 강제로 소프트 재부팅:

`systemctl soft-reboot {{[-f|--force]}}`

- 특정 시간에 소프트 재부팅 예약:

`systemctl soft-reboot --when "{{타임스탬프}}"`

- 예약된 소프트 재부팅 취소:

`systemctl soft-reboot --when cancel`
