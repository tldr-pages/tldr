# npm install

> Node paketleri kurmayı sağlar.
> Daha fazla bilgi: <https://docs.npmjs.com/cli/commands/npm-install>.

- `package.json` dosyasında listelenen bağımlılıkları kurar:

`npm install`

- Bir paketin spesifik bir versiyonunu indirir ve `package.json` dosyasındaki bağımlılık listesine ekler:

`npm install {{package_name}}@{{version}}`

- Paketin son sürümünü indirir ve `package.json` dosyasındaki geliştirme bağımlılık listesine ekler:

`npm install {{package_name}} {{-D|--save-dev}}`

- Paketin son sürümünü indirir ve global olarak kurar:

`npm install {{-g|--global}} {{package_name}}`
