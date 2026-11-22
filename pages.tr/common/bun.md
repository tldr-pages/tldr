# bun

> JavaScript çalışma zamanı ortamı ve araç seti.
> Bir paketleyici (bundler), bir test çalıştırıcı ve bir paket yöneticisi içerir.
> Daha fazla bilgi: <https://bun.com/docs>.

- Geçerli dizinde yeni bir Bun projesi oluştur:

`bun init`

- Bir JavaScript dosyasını veya `package.json` betiğini çalıştır:

`bun run {{dosya/yolu|betik_adı}}`

- Birim testlerini çalıştır:

`bun test`

- Belirtilen `package.json` dosyasında listelenen tüm bağımlılıkları indir ve kur:

`bun {{[i|install]}}`

- Belirtilen `package.json` dosyasına bir bağımlılık ekle:

`bun {{[a|add]}} {{modül_adı}}`

- Belirtilen `package.json` dosyasından bir bağımlılığı kaldır:

`bun {{[rm|remove]}} {{modül_adı}}`

- Bir REPL (etkileşimli kabuk) başlat:

`bun repl`

- Bun'ı en son sürüme yükselt:

`bun upgrade`
