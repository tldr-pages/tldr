# secrethub

> Egy eszköz, amellyel a konfigurációs fájlok titkai távol tarthatók a konfigurációs fájlokból. További információ: <https://secrethub.io>.

- Titok nyomtatása a `stdout` címre:

`secrethub read {{path/to/secret}}`

- Egy véletlen érték generálása és tárolása új vagy frissített titokként:

`secrethub generate {{path/to/secret}}`

- Egy érték tárolása a vágólapról új vagy frissített titokként:

`secrethub write --clip {{path/to/secret}}`

- A `stdin` oldalon megadott érték új vagy frissített titokként való tárolása:

`echo "{{secret_value}}" | secrethub write {{path/to/secret}}`

- Adattár vagy titok ellenőrzése:

`secrethub audit {{path/to/repo_or_secret}}`
