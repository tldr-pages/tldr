# npx

> `npm` paketlerinden komutlar çalıştırır.
> Daha fazla bilgi için: <https://github.com/npm/npx>.

- Lokal veya uzaktaki bir `npm` paketinden komut çalıştırır:

`npx {{komut}} {{argüman1 argüman2 ...}}`

- Aynı isimde birden fazla komut varsa, paketi açıkça belirtmek mümkün:

`npx --package {{paket}} {{komut}}`

- Bir komut şu anki dizinde veya `node_modules/.bin` içinde varsa çalıştırır:

`npx --no-install {{komut}} {{argüman1 argüman2 ...}}`

- `npx`'in çıktısını gizleyerek belirli bir komutu çalıştırır:

`npx --quiet {{komut}} {{argüman1 argüman2 ...}}`

- Yardım görüntüle:

`npx --help`
