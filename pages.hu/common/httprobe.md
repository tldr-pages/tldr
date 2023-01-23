# httprobe

> Vegyen egy listát a tartományokról, és keressen működő HTTP- és HTTPS-kiszolgálókat. További információ: <https://github.com/tomnomnom/httprobe>.

- Tartományok listájának vizsgálata egy szöveges fájlból:

`cat {{input_file}} | httprobe`

- Csak akkor ellenőrizze a HTTP-t, ha a HTTPS nem működik:

`cat {{input_file}} | httprobe --prefer-https`

- További portok szondázása egy adott protokollal:

`cat {{input_file}} | httprobe -p {{https:2222}}`

- Az összes rendelkezésre álló opció kiadása:

`httprobe --help`
