# systemsetup

> 시스템 환경설정 기기 설정 구성.
> 더 많은 정보: <https://support.apple.com/guide/remote-desktop/about-systemsetup-apd95406b8d/mac>.

- 원격 로그인(SSH) 활성화:

`systemsetup -setremotelogin on`

- 시간대, NTP 서버 지정 및 네트워크 시간 활성화:

`systemsetup -settimezone "{{US/Pacific}}" -setnetworktimeserver {{us.pool.ntp.org}} -setusingnetworktime on`

- 기기를 절대 절전 모드로 두지 않으며 전원 장애나 커널 패닉 시 자동으로 재시작:

`systemsetup -setsleep off -setrestartpowerfailure on -setrestartfreeze on`

- 유효한 시작 디스크 나열:

`systemsetup -liststartupdisks`

- 새로운 시작 디스크 지정:

`systemsetup -setstartupdisk {{경로/대상/폴더}}`
