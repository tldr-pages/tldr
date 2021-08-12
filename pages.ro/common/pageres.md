# pageres

> Capturați capturi de ecran ale site-urilor web în diferite rezoluții.
> Mai multe informaţii: <https://github.com/sindresorhus/pageres-cli>

- Ia mai multe capturi de ecran de mai multe URL-uri la rezoluții diferite:

`pageres {{https://example.com/}} {{https://example2.com/}} {{1366x768}} {{1600x900}}`

- Furnizarea de opțiuni specifice pentru un URL, suprascrierea opțiunilor globale:

`pageres [{{https://example.com/}} {{1366x768}} --no-crop] [{{https://example2.com/}} {{1024x768}}] --crop`

- Furnizați un șablon de nume de fișier personalizat:

`pageres {{https://example.com/}} {{1024x768}} --filename={{'<%= date %> - <%= url %>'}}`

- Capturează un anumit element pe o pagină:

`pageres {{https://example.com/}} {{1366x768}} --selector='{{.page-header}}'`

- Ascundeți un element specific:

`pageres {{https://example.com/}} {{1366x768}} --hide='{{.page-header}}'`

- Capturați o captură de ecran a unui fișier local:

`pageres {{local_file_path.html}} {{1366x768}}`
