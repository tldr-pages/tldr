# onionsearch

> Scrape URLs on different `.onion` search engines.
> `onionsearch` requires tor proxy running on `localhost:9050`.
> A tor enabled browser is needed to visit the .onion websites.
> More information: <https://github.com/megadose/OnionSearch>.

- Request all the search engines for the word "Epstein":

`onionsearch "Epstein"`

- Request search results from specific search engines:

`onionsearch "{{Lolita Island}}" --engines {{tor66 deeplink phobos ...}}`

- Exclude certain serarch engines when searching:

`onionsearch "{{Hunter Biden}}" --exclude {{candle ahmia ...}}`

- Limit the number of pages to load per engine:

`onionsearch "{{stuxnet}}" --engines {{tor66 deeplink phobos ...}} --limit {{3}}`

- List of supported search engines:

`onionsearch --help | grep -A1 -i "supported engines"`
