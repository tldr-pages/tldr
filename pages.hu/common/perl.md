# perl

> A Perl 5 nyelvi interpreter. További információ: <https://www.perl.org>.

- Egy Perl szkript elemzése és végrehajtása:

`perl {{script.pl}}`

- Egy Perl szkript szintaktikai hibáinak ellenőrzése:

`perl -c {{script.pl}}`

- Perl utasítás elemzése és végrehajtása:

`perl -e {{perl_statement}}`

- Perl szkript futtatása hibakeresési módban a `perldebug` segítségével:

`perl -d {{script.pl}}`

- Az összes fájlsor szerkesztése \[i\]n-place egy adott helyettesítő \[e\]xpressionnel, mentve egy biztonsági másolatot új kiterjesztéssel:

`perl -p -i'.{{extension}}' -e 's/{{regular_expression}}/{{replacement}}/g' {{path/to/file}}`

- Többsoros \[e\]xpression futtatása egy fájlon, és az eredmény mentése egy adott fájlba:

`perl -p -e 's/{{foo\nbar}}/{{foobar}}/g' {{path/to/input_file}} > {{path/to/output_file}}`

- Szabályos \[e\]xpression futtatása a `stdin` oldalon, a megfelelő \[l\]inek kinyomtatása:

`cat {{path/to/file}} | perl -n -l -e 'print if /{{regular_expression}}/'`

- Futtasson egy reguláris \[e\]xpressiont a `stdin` oldalon, minden egyes megfelelő \[l\]ine esetében csak az első rögzítési csoportot nyomtatva ki:

`cat {{path/to/file}} | perl -n -l -e 'print $1 if /{{before}}({{regular_expression}}){{after}}/'`
