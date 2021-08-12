# web-ext

> Un instrument de linie de comandă pentru gestionarea dezvoltării extensiilor web.
> Mai multe informaţii: <https://www.npmjs.com/package/web-ext>

- Rulați extensia web în directorul curent din Firefox:

`web-ext run`

- Rulați o extensie web dintr-un anumit director în Firefox:

`web-ext run --source-dir {{path/to/directory}}`

- Afișează ieșirea de execuție verbose:

`web-ext run --verbose`

- Rulați o extensie web în Firefox Android:

`web-ext run --target firefox-android`

- Lint fişierele manifest şi sursă pentru erori:

`web-ext lint`

- Construiți și împachetați extensia:

`web-ext build`

- Afișează ieșirea compilării verbose:

`web-ext build --verbose`

- Semnați un pachet pentru auto-găzduire:

`web-ext sign --api-key {{api_key}} --api-secret {{api_secret}}`
