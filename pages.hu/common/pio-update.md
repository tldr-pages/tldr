# pio update

> A telepített PlatformIO Core csomagok, fejlesztési platformok és globális könyvtárak frissítése. Lásd még: `pio platform update`, `pio lib update`. További információ: [https://docs.platformio.org/en/latest/core/userguide/cmd_update.html.](https://docs.platformio.org/en/latest/core/userguide/cmd_update.html)

- Végezze el az összes csomag, fejlesztési platform és globális könyvtár teljes frissítését:

`pio update`

- Csak a core csomagok frissítése (kihagyja a platformokat és a könyvtárakat):

`pio update --core-packages`

- A csomagok, platformok és könyvtárak új verzióinak ellenőrzése, de tényleges frissítésük nem történik:

`pio update --dry-run`
