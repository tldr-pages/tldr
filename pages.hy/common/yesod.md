#այո

> Օգնական գործիք Yesod-ի համար՝ Haskell-ի վրա հիմնված վեբ շրջանակ:.
> Yesod-ի բոլոր հրամանները կանչվում են `stack` ծրագրի կառավարչի միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/yesodweb/yesod>:.

- Ստեղծեք նոր փայտամած կայք՝ SQLite-ի հետ միասին, `my-project` գրացուցակում.:

`stack new {{my-project}} {{yesod-sqlite}}`

- Տեղադրեք Yesod CLI գործիքը Yesod փայտամած կայքում.:

`stack build yesod-bin cabal-install --install-ghc`

- Սկսեք զարգացման սերվերը.:

`stack exec -- yesod devel`

- Հպեք ֆայլեր փոփոխված կաղապարի Haskell կախվածությամբ.:

`stack exec -- yesod touch`

- Տեղադրեք հավելվածը, օգտագործելով Keter-ը (Yesod-ի տեղակայման մենեջեր).:

`stack exec -- yesod keter`
