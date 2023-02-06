# halt

> Állítsa le a rendszert. További információ: <https://www.man7.org/linux/man-pages/man8/halt.8.html>.

- Állítsa le a rendszert:

`halt`

- A rendszer kikapcsolása (ugyanaz, mint a `poweroff`):

`halt --poweroff`

- A rendszer újraindítása (ugyanaz, mint a `reboot`):

`halt --reboot`

- Azonnali leállítás a rendszerfelügyelővel való kapcsolatfelvétel nélkül:

`halt --force --force`

- A wtmp shutdown bejegyzés írása a rendszer leállítása nélkül:

`halt --wtmp-only`
