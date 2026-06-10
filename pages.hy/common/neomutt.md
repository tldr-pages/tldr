# neomutt

> NeoMutt էլփոստի հաճախորդ:.
> Լրացուցիչ տեղեկություններ. <https://neomutt.org/guide/reference.html>:.

- Բացեք նշված փոստարկղը.:

`neomutt -f {{path/to/mailbox}}`

- Սկսեք նամակ գրել և նշեք թեման և `cc` ստացողը՝:

`neomutt -s "{{subject}}" -c {{cc@example.com}} {{recipient@example.com}}`

- Ուղարկեք նամակ կից ֆայլերով.:

`neomutt -a {{path/to/file1 path/to/file2 ...}} -- {{recipient@example.com}}`

- Նշեք ֆայլ, որը ներառելու է որպես հաղորդագրության մարմին.:

`neomutt -i {{path/to/file}} {{recipient@example.com}}`

- Նշեք հաղորդագրության վերնագիրն ու հիմնականը պարունակող ֆայլի նախագիծ՝ RFC 5322 ձևաչափով.:

`neomutt -H {{path/to/file}} {{recipient@example.com}}`
