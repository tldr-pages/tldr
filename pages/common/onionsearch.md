# onionsearch

> Scrape URLs on different `.onion` search engines.
> Note: `onionsearch` requires a Tor proxy running on `localhost:9050`; a Tor enabled browser is needed to visit the `.onion` websites.
> More information: <https://github.com/megadose/OnionSearch>.

- Request results from all the search engines:

`onionsearch "{{string}}"`

- Request search results from specific search engines:

`onionsearch "{{string}}" --engines {{tor66 deeplink phobos ...}}`

- Exclude certain search engines when searching:

`onionsearch "{{string}}" --exclude {{candle ahmia ...}}`

- Limit the number of pages to load per engine:

`onionsearch "{{stuxnet}}" --engines {{tor66 deeplink phobos ...}} --limit {{3}}`

- List all supported search engines:

`onionsearch --help | grep {{[-A|--after-context]}} 1 {{[-i|--ignore-case]}} "supported engines"`
