# jj կիսատ

> Գտեք վատ վերանայում ըստ բաժանման:.
> Լրացուցիչ տեղեկություններ. <https://docs.jj-vcs.dev/latest/cli-reference/#jj-bisect>:.

- Գտեք տիրույթում առաջին վատ տարբերակը՝ գործարկելով թեստային հրաման.:

`jj bisect run {{[-r|--range]}} {{good_revision}}..{{bad_revision}} {{command}}`

- Գտեք առաջին վատ տարբերակը՝ օգտագործելով shell հրամանը.:

`jj bisect run {{[-r|--range]}} {{good_revision}}..{{bad_revision}} -- bash -c "{{command}}"`

- Գտեք առաջին լավ վերանայումը առաջին վատի փոխարեն.:

`jj bisect run {{[-r|--range]}} {{good_revision}}..{{bad_revision}} --find-good {{command}}`

- Գտեք առաջին տարբերակը, որտեղ ավելացվել է ֆայլ.:

`jj bisect run {{[-r|--range]}} {{good_revision}}..{{bad_revision}} --find-good -- test -f {{path/to/file}}`
