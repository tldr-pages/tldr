# բեռնախցիկ

> Փաթեթավորեք և սպասարկեք Rust WASM վեբ հավելվածները:.
> Լրացուցիչ տեղեկություններ. <https://trunkrs.dev/commands/>:.

- Կառուցեք հավելվածը թողարկման ռեժիմում և սպասարկեք այն տեղում.:

`trunk serve --release`

- Կառուցեք հավելվածը և սպասարկեք այն հատուկ նավահանգստում.:

`trunk serve {{[-p|--port]}} {{port}}`

- Ստեղծեք արտադրության համար հատուկ ելքային գրացուցակում.:

`trunk build --release {{[-d|--dist]}} {{path/to/distribution}}`

- Կառուցեք ենթագրքում հոսթինգի հատուկ հանրային URL ուղիով.:

`trunk build --release --public-url /{{path/to/app_subdirectory}}`

- Մաքրել ելքային գրացուցակը.:

`trunk clean`
