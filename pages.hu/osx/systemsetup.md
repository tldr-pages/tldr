# systemsetup

> A rendszerbeállítások gépi beállításainak konfigurálása. További információ: <https://support.apple.com/guide/remote-desktop/about-systemsetup-apd95406b8d/mac>.

- Engedélyezze a távoli bejelentkezést (SSH):

`systemsetup -setremotelogin on`

- Adja meg az időzónát, az NTP-kiszolgálót és engedélyezze a hálózati időt:

`systemsetup -settimezone "{{US/Pacific}}" -setnetworktimeserver {{us.pool.ntp.org}} -setusingnetworktime on`

- Állítsa be, hogy a gép soha ne aludjon el, és automatikusan induljon újra áramkimaradás vagy kernelpánik esetén:

`systemsetup -setsleep off -setrestartpowerfailure on -setrestartfreeze on`

- Listázza az érvényes indítólemezeket:

`systemsetup -liststartupdisks`

- Új indítólemez megadása:

`systemsetup -setstartupdisk {{path}}`
