# var-dump-server

> Symfony dump server.
> Colectează datele care fac obiectul unui dumping de componenta Symfony VarDumper.
> Mai multe informaţii: <https://symfony.com/doc/current/components/var_dumper.html#the-dump-server>

- Porniţi serverul:

`var-dump-server`

- Dump datele într-un fișier HTML:

`var-dump-server --format=html > {{path/to/file.html}}`

- Asigurați-server asculta pe o anumită adresă și port:

`var-dump-server --host {{127.0.0.1:9912}}`
