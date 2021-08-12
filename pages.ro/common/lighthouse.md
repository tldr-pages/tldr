# lighthouse

> Analizează aplicațiile web și paginile web, colectând valori moderne de performanță și informații despre cele mai bune practici ale dezvoltatorilor.
> Mai multe informaţii: <https://github.com/GoogleChrome/lighthouse>

- Generați un raport HTML pentru un anumit site web și salvați-l într-un fișier din directorul curent:

`lighthouse {{https://example.com}}`

- Generați un raport JSON și imprimați-l:

`lighthouse --output {{json}} {{https://example.com}}`

- Generați un raport JSON și salvați-l într-un anumit fișier:

`lighthouse --output {{json}} --output-path {{path/to/file.json}} {{https://example.com}}`

- Generați un raport utilizând browserul în modul fără cap fără a vă conecta la stdout:

`lighthouse --quiet --chrome-flags="{{--headless}}" {{https://example.com}}`

- Generați un raport, utilizând perechile de cheie/valoare HTTP din fișierul JSON specificat pentru toate solicitările:

`lighthouse --extra-headers={{path/to/file.json}} {{https://example.com}}`

- Generarea unui raport numai pentru anumite categorii:

`lighthouse --only-categories={{performance,accessibility,best-practices,seo,pwa}} {{https://example.com}}`

- Generați un raport cu emularea dispozitivului și toate limitările dezactivate:

`lighthouse --screenEmulation.disabled --throttling-method={{provided}} --no-emulatedUserAgent {{https://example.com}}`

- Ajutor pentru afișare:

`lighthouse --help`
