# ntp-ctl

> `ntpd-rs` 데몬을 관리하는 클라이언트.
> 더 많은 정보: <https://docs.ntpd-rs.pendulum-project.org/man/ntp-ctl.8/>.

- 현재 NTP 데몬의 상태 정보 표시:

`ntp-ctl status`

- 지정한 설정 파일 (기본값: `/etc/ntpd-rs/ntp.toml`)의 유효성 검사:

`ntp-ctl {{[-c|--config]}} {{경로/대상/설정파일}} validate`

- 시계를 한 번 강제로 동기화를 대화형으로 실행:

`sudo ntp-ctl force-sync`
