# opkg

> Egy könnyű csomagkezelő, amely az OpenWrt csomagok telepítésére szolgál. További információ: <https://openwrt.org/docs/guide-user/additional-software/opkg>.

- Csomag telepítése:

`opkg install {{package}}`

- Csomag eltávolítása:

`opkg remove {{package}}`

- Az elérhető csomagok listájának frissítése:

`opkg update`

- Az összes telepített csomag frissítése:

`opkg upgrade`

- Egy vagy több konkrét csomag(ok) frissítése:

`opkg upgrade {{package(s)}}`

- Egy adott csomagra vonatkozó információk megjelenítése:

`opkg info {{package}}`

- Az összes elérhető csomag listázása:

`opkg list`
