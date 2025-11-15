# timedatectl

> 시스템 시간과 날짜를 제어합니다.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/timedatectl.html>.

- 현재 시스템 시계 시간 확인:

`timedatectl`

- 시스템 시계의 로컬 시간을 직접 설정:

`timedatectl set-time "{{yyyy-MM-dd hh:mm:ss}}"`

- 사용 가능한 시간대 나열:

`timedatectl list-timezones`

- 시스템 시간대 설정:

`timedatectl set-timezone {{시간대}}`

- 네트워크 시간 프로토콜(NTP) 동기화 활성화:

`timedatectl set-ntp on`

- 하드웨어 시계 시간 기준을 로컬 시간으로 변경:

`timedatectl set-local-rtc 1`
