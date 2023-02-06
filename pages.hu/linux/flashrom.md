# flashrom

> Flash chipek olvasása, írása, ellenőrzése és törlése. További információ: <https://manned.org/flashrom>.

- Szondázza meg a chipet, és győződjön meg arról, hogy a vezetékezés megfelelő:

`flashrom --programmer {{programmer}}`

- Olvassa ki a flash chipet és mentse el egy fájlba:

`flashrom -p {{programmer}} --read {{path/to/file}}`

- Fájl írása a flashre:

`flashrom -p {{programmer}} --write {{path/to/file}}`

- A flash ellenőrzése egy fájl alapján:

`flashrom -p {{programmer}} --verify {{path/to/file}}`

- A chip szondázása Raspberry Pi segítségével:

`flashrom -p {{linux_spi:dev=/dev/spidev0.0}}`
