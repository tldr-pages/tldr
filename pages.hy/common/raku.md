#ռակու

> Rakudo Raku (նախկինում Perl 6) ծրագրավորման լեզվի թարգմանիչ:.
> Տես նաև՝ `perl`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/raku>:.

- Կատարեք Raku սցենար.:

`raku {{path/to/script.raku}}`

- Կատարեք մեկ Raku հրաման.:

`raku -e "{{command}}"`

- Ստուգեք միայն շարահյուսությունը (աշխատում է BEGIN և CHECK բլոկները).:

`raku -c {{path/to/script.raku}}`

- Սկսեք REPL (ինտերակտիվ կեղև).:

`raku`

- Ծրագիրը գործարկելուց առաջ բեռնեք մոդուլ.:

`raku -M {{module_name}} {{path/to/script.raku}}`

- Ավելացնել ուղի մոդուլի որոնման ճանապարհին.:

`raku -I {{path/to/module_directory}} {{path/to/script.raku}}`

- Քաղեք և ցուցադրեք փաստաթղթերը սցենարից.:

`raku --doc {{path/to/script.raku}}`
