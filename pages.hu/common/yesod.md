# yesod

> Segédeszköz a Yesod-hoz, egy Haskell-alapú webes keretrendszerhez. Minden Yesod parancsot a `stack` projektmenedzser segítségével hívhatunk meg. További információ: <https://github.com/yesodweb/yesod>.

- Hozzon létre egy új scaffolded webhelyet, SQLite-tel mint backenddel, a `my-project` könyvtárban:

`stack new {{my-project}} {{yesod-sqlite}}`

- Telepítse a Yesod CLI eszközt egy Yesod scaffolded site-on belül:

`stack build yesod-bin cabal-install --install-ghc`

- Indítsa el a fejlesztői szervert:

`stack exec -- yesod devel`

- Érintse meg a módosított Template Haskell függőségekkel rendelkező fájlokat:

`stack exec -- yesod touch`

- Az alkalmazás telepítése a Keter (Yesod telepítési menedzser) segítségével:

`stack exec -- yesod keter`
