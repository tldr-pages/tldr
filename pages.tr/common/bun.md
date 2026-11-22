# bun

> JavaScript çalışma zamanı ve araç seti.
> Bir paketleyici (bundler), bir test çalıştırıcı ve bir paket yöneticisi içerir.
> Daha fazla bilgi için: <https://bun.com/docs>.

- Geçerli dizinde yeni bir Bun projesi oluştur:

`bun init`

- Bir JavaScript dosyasını veya bir `package.json` betiğini çalıştır:

`bun run {{dosya/yolu/veya/betik_adı}}`

- Birim testlerini çalıştır:

`bun test`

- Bağımlılık olarak listelenen tüm paketleri indir ve kur:

`bun {{[i|install]}}`

- Yeni bir bağımlılık ekle:

`bun {{[a|add]}} {{modül_adı}}`

- Bir bağımlılığı kaldır:

`bun {{[rm|remove]}} {{modül_adı}}`

- Bir REPL (etkileşimli kabuk) başlat:

`bun repl`

- Bun'ı en son sürüme yükselt:

`bun upgrade`
