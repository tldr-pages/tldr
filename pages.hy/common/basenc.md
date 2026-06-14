# բազային

> Կոդավորեք կամ վերծանեք ֆայլը կամ `stdin`՝ օգտագործելով նշված կոդավորումը՝ `stdout`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/basenc-invocation.html>:.

- Կոդավորեք ֆայլը base64 կոդավորմամբ.:

`basenc --base64 {{path/to/file}}`

- Վերծանեք ֆայլը base64 կոդավորմամբ.:

`basenc {{[-d|--decode]}} --base64 {{path/to/file}}`

- Կոդավորում `stdin`-ից՝ base32 կոդավորմամբ՝ 42 սյունակով.:

`{{command}} | basenc --base32 {{[-w|--wrap]}} 42`

- Կոդավորում `stdin`-ից՝ base32 կոդավորմամբ.:

`{{command}} | basenc --base32`
