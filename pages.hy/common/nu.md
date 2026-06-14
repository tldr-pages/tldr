# nu

> Nushell-ը («կեղևի նոր տեսակ») ժամանակակից, կառուցվածքային մոտեցում է ցուցաբերում ձեր հրամանի տողին:.
> Տես նաև՝ `elvish`:.
> Լրացուցիչ տեղեկություններ. <https://www.nushell.sh/book/configuration.html#flag-behavior>:.

- Սկսեք ինտերակտիվ shell նստաշրջան.:

`nu`

- Կատարել հատուկ հրամաններ.:

`nu {{[-c|--commands]}} "{{echo 'nu is executed'}}"`

- Կատարել կոնկրետ սցենար.:

`nu {{path/to/script.nu}}`

- Կատարեք հատուկ սցենար լոգինգով.:

`nu --log-level {{error|warn|info|debug|trace}} {{path/to/script.nu}}`
