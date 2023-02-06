# fwupdmgr

> Eszköz az eszköz firmware frissítésére, beleértve az UEFI-t is, a `fwupd` segítségével. További információ: <https://fwupd.org/>.

- Az fwupd által észlelt összes eszköz megjelenítése:

`fwupdmgr get-devices`

- A legújabb firmware metaadatok letöltése az LVFS-ből:

`fwupdmgr refresh`

- A rendszerben lévő eszközökhöz elérhető frissítések listája:

`fwupdmgr get-updates`

- A firmware frissítések telepítése:

`fwupdmgr update`
