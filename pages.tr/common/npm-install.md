# npm install

> Node paketleri kurmayı sağlar.
> Daha fazla bilgi için: <https://docs.npmjs.com/cli/npm-install>.

- `package.json` dosyasında listelenen bağımlılıkları kurar:

`npm install`

- Bir paketin spesifik bir versiyonunu indirir ve `package.json` dosyasındaki bağımlılık listesine ekler:

`npm install {{paket_adı}}@{{versiyon}}`

- Paketin son sürümünü indirir ve `package.json` dosyasındaki geliştirme bağımlılık listesine ekler:

`npm install {{paket_adı}} {{-D|--save-dev}}`

- Paketin son sürümünü indirir ve global olarak kurar:

`npm install {{-g|--global}} {{paket_adı}}`
