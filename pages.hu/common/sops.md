# sops

> SOPS: Titkok OPerationS. A titkok kezelésére szolgáló eszköz. További információ: <https://github.com/mozilla/sops>.

- Egy fájl titkosítása:

`sops -e {{path/to/myfile.json}} > {{path/to/myfile.enc.json}}`

- Egy fájl visszafejtése a szabványos kimenetre:

`sops -d {{path/to/myfile.enc.json}}`

- Adatkulcsok forgatása egy sops fájlhoz:

`sops -r {{path/to/myfile.enc.yaml}}`

- A titkosított fájl kiterjesztésének módosítása:

`sops -d --input-type json {{path/to/myfile.enc.json}}`

- A kulcsok kivonása elnevezéssel, a tömbelemek számozással:

`sops -d --extract '["an_array"][1]' {{path/to/myfile.enc.json}}`

- Két sops fájl közötti különbség megjelenítése:

`diff <(sops -d {{path/to/secret1.enc.yaml}}) <(sops -d {{path/to/secret2.enc.yaml}})`
