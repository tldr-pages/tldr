# yarn

> JavaScript és Node.js csomagkezelő alternatíva. További információ: <https://yarnpkg.com>.

- Egy modul globális telepítése:

`yarn global add {{module_name}}`

- Telepítse az összes függőséget, amelyre a `package.json` fájlban hivatkozik (a `install` opcionális):

`yarn install`

- Telepítsen egy modult, és mentse függőségként a `package.json` fájlba (a `--dev` hozzáadása a dev függőségként való mentéshez):

`yarn add {{module_name}}@{{version}}`

- Egy modul eltávolítása és eltávolítása a `package.json` fájlból:

`yarn remove {{module_name}}`

- Interaktívan létrehozhat egy `package.json` fájlt:

`yarn init`

- Annak megállapítása, hogy egy modul függőségi viszonyban van-e, és a tőle függő modulok listázása:

`yarn why {{module_name}}`
