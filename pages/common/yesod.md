# yesod

> A framework to develop Haskell web applications.
> All yesod commands are invoked through the `stack` project manager.

- Create a new scaffolded site with sqlite as backend in `my-project` directory:

`stack new {{my-project}} {{yesod-sqlite}}`

- Install the Yesod CLI tool within a Yesod scaffolded site:

`stack build yesod-bin cabal-install --install-ghc`

- Start development server:

`stack exec -- yesod devel`

- Touch files with altered Template Haskell dependencies:

`stack exec -- yesod touch`

- Deploy application using Keter (Yesod's deployment manager):

`stack exec -- yesod keter`
