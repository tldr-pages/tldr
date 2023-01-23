# AdGuardHome

> Hálózati szintű szoftver a hirdetések és a nyomkövetés blokkolására. További információ: <https://github.com/AdguardTeam/AdGuardHome>.

- AdGuard Home futtatása:

`AdGuardHome`

- Az AdGuard Home futtatása egy adott konfigurációval:

`AdGuardHome --config {{path/to/AdGuardHome.yaml}}`

- Állítsa be a munkakönyvtárat, amelyben az adatokat tárolja:

`AdGuardHome --work-dir {{path/to/directory}}`

- Az AdGuard Home szolgáltatásként történő telepítése vagy eltávolítása:

`AdGuardHome --service {{install|uninstall}}`

- Az AdGuard Home szolgáltatás elindítása:

`AdGuardHome --service start`

- Az AdGuard Home szolgáltatás konfigurációjának újratöltése:

`AdGuardHome --service reload`

- Az AdGuard Home szolgáltatás leállítása vagy újraindítása:

`AdGuardHome --service {{stop|restart}}`
