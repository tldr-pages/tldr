# pio home

> Indítsa el a PlatformIO Home webszerverét. További információ: <https://docs.platformio.org/en/latest/core/userguide/cmd_home.html>.

- Nyissa meg a PlatformIO Home-ot az alapértelmezett webböngészőben:

`pio home`

- Használjon egy adott HTTP-portot (alapértelmezés szerint 8008):

`pio home --port {{port}}`

- Kötődjön egy adott IP-címhez (alapértelmezés szerint 127.0.0.0.1):

`pio home --host {{ip_address}}`

- Ne nyissa meg automatikusan a PlatformIO Home-ot az alapértelmezett webböngészőben:

`pio home --no-open`

- Automatikusan leállítja a kiszolgálót az időkorlátozáskor (másodpercben), ha nincs csatlakozó ügyfél:

`pio home --shutdown-timeout {{time}}`

- Egyedi munkamenet-azonosító megadása a PlatformIO Home más példányoktól való elkülönítése és a harmadik felek hozzáférésétől való védelme érdekében:

`pio home --session-id {{id}}`
