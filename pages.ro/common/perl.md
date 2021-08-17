# perl

> Interpretul de limbă Perl 5.
> Mai multe informaţii: <https://www.perl.org>

- Analizaţi şi executaţi un script Perl:

`perl {{script.pl}}`

- Verificați erorile de sintaxă pe un script Perl:

`perl -c {{script.pl}}`

- Analizaţi şi executaţi o declaraţie Perl:

`perl -e {{perl_statement}}`

- Rulați un script Perl în modul de depanare, folosind `perldebug`:

`perl -d {{script.pl}}`

- [p]entru toate liniile unui fișier, editarea lor d[i]rect în fișier folosind o [e]xpresie de căutare/înlocuit:

`perl -p -i -e 's/{{find}}/{{replace}}/g' {{filename}}`

- Rulați o expresie găsire/înlocuire pe un fișier, salvând fișierul original cu o extensie dată:

`perl -p -i'.old' -e 's/{{find}}/{{replace}}/g' {{filename}}`

- Rulați o expresie de găsire/înlocuire pe un fișier și salvați rezultatul într-un alt fișier:

`perl -p0e 's/{{foo\nbar}}/{{foobar}}/g' {{input_file}} > {{output_file}}`

- Rulați o expresie regulată pe stdin, tipăriți primul grup de captură pentru fiecare linie:

`cat {{path/to/input_file}} | perl -nle 'if (/.*({{foo}}).*/) {print "$1"; last;}'`
