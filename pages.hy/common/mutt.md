#մութ

> Հրամանատարի էլփոստի հաճախորդ:.
> Լրացուցիչ տեղեկություններ. <http://mutt.org/doc/mutt.1.txt>:.

- Բացեք նշված փոստարկղը.:

`mutt -f {{mailbox}}`

- Ուղարկեք նամակ և նշեք թեման և cc ստացողին.:

`mutt -s {{subject}} -c {{cc@example.com}} {{recipient@example.com}}`

- Ուղարկեք նամակ կից ֆայլերով.:

`mutt -a {{file1 file2 ...}} -- {{recipient@example.com}}`

- Նշեք ֆայլ, որը ներառելու է որպես հաղորդագրության մարմին.:

`mutt -i {{path/to/file}} {{recipient@example.com}}`

- Նշեք հաղորդագրության վերնագիրն ու հիմնականը պարունակող ֆայլի նախագիծ՝ RFC 5322 ձևաչափով.:

`mutt -H {{path/to/file}} {{recipient@example.com}}`
