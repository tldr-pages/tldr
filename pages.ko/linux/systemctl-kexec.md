# systemctl kexec

> kexec를 사용하여 시스템을 재부팅.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#kexec>.

- kexec를 이용한 빠른 재부팅 (커널이 미리 로드된 경우):

`systemctl kexec`

- kexec가 가능하더라도 일반 재부팅 강제 실행:

`systemctl kexec {{[-f|--force]}}`
