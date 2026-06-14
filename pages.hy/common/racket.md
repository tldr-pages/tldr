#ռակետ

> Ռակետ լեզվի թարգմանիչ:.
> Լրացուցիչ տեղեկություններ. <https://docs.racket-lang.org/reference/running-sa.html#%28part._mz-cmdline%29>:.

- Սկսեք REPL (ինտերակտիվ կեղև).:

`racket`

- Կատարել Racket սցենար.:

`racket {{path/to/script.rkt}}`

- Կատարեք Racket արտահայտությունը.:

`racket {{[-e|--eval]}} "{{expression}}"`

- Գործարկել մոդուլը որպես սցենար (վերջացնում է ընտրանքների ցանկը).:

`racket {{[-l|--lib]}} {{module_name}} {{[-m|--main]}} {{arguments}}`

- Սկսեք REPL (ինտերակտիվ կեղև) `typed/racket` հեշլանգի համար.:

`racket -I typed/racket`
