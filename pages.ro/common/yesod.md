# yesod

> Instrument Helper pentru Yesod, un cadru web bazat pe Haskell.
> Toate comenzile Yesod sunt invocate prin intermediul managerului de proiect `stiva”.
> Mai multe informaţii: <https://github.com/yesodweb/yesod>

- Creați un nou site de schele, cu sqlite ca backend, în directorul `my-project`:

`stack new {{my-project}} {{yesod-sqlite}}`

- Instalați instrumentul Yesod CLI într-un site de schele Yesod:

`stack build yesod-bin cabal-install --install-ghc`

- Start server de dezvoltare:

`stack exec -- yesod devel`

- Touch fișiere cu dependențe modificate Template Haskell:

`stack exec -- yesod touch`

- Implementați aplicația utilizând Keter (managerul de implementare al lui Yesod):

`stack exec -- yesod keter`
