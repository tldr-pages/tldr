# npm

> JavaScript ve Node.js paket yöneticisi.
> Node.js projelerini ve modül bağımlılıklarını yönet.
> `install`, `run` gibi bazı alt komutların kendi kullanım dokümantasyonu vardır.
> Daha fazla bilgi için: <https://docs.npmjs.com/cli/npm/>.

- Varsayılan değerlerle bir `package.json` dosyası oluştur (etkileşimli yapmak için `--yes` kullanma):

`npm init {{[-y|--yes]}}`

- Bağımlılık olarak `package.json` dosyasında listelenen tüm paketleri indir:

`npm {{[i|install]}}`

- Bir paketin belirli bir sürümünü indir ve `package.json` dosyasındaki bağımlılık listesine ekle:

`npm {{[i|install]}} {{paket_adı}}@{{sürüm}}`

- Bir paketin son sürümünü indir ve `package.json` dosyasındaki geliştirme bağımlılıkları listesine ekle:

`npm {{[i|install]}} {{paket_adı}} {{[-D|--save-dev]}}`

- Bir paketin son sürümünü indir ve global olarak kur (kurulum konumunu `npm config set prefix` ile ayarla):

`npm {{[i|install]}} {{paket_adı}} {{[-g|--global]}}`

- Bir paketi kaldır ve `package.json` dosyasındaki bağımlılık listesinden çıkar:

`npm {{[r|uninstall]}} {{paket_adı}}`

- Yerel olarak kurulu tüm bağımlılıkları listele:

`npm {{[ls|list]}}`

- Global olarak kurulu tüm üst düzey paketleri listele:

`npm {{[ls|list]}} {{[-g|--global]}} --depth {{0}}`
