# npx

> `npm` paketlerinden komutlar çalıştırır.
> Daha fazla bilgi için: <https://github.com/npm/npx>.

- Lokal veya uzaktaki bir `npm` paketinden komut çalıştırır:

`npx {{command}} {{argument1 argument2 ...}}`

- Aynı isimde birden fazla komut varsa, paketi açıkça belirtmek mümkün:

`npx --package {{package}} {{command}}`

- Bir komut şu anki dizinde veya `node_modules/.bin` içinde varsa çalıştırır:

`npx --no-install {{command}} {{argument1 argument2 ...}}`

- `npx`'in çıktısını gizleyerek belirli bir komutu çalıştırır:

`npx --quiet {{command}} {{argument1 argument2 ...}}`

- Yardım görüntüle:

`npx --help`
