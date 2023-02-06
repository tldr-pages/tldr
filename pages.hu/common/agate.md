# agate

> Egy egyszerű szerver a Gemini hálózati protokollhoz. További információ: <https://github.com/mbrubeck/agate>.

- Futtasson és generáljon privát kulcsot és tanúsítványt:

`agate --content {{path/to/content/}} --addr {{[::]:1965}} --addr {{0.0.0.0:1965}} --hostname {{example.com}} --lang {{en-US}}`

- Kiszolgáló futtatása:

`agate {{path/to/file}}`

- Súgó megjelenítése:

`agate -h`
