# var-dump-server

> Symfony dump szerver. Összegyűjti a Symfony VarDumper komponens által dumpolt adatokat. További információ: <https://symfony.com/doc/current/components/var_dumper.html#the-dump-server>.

- Indítsa el a kiszolgálót:

`var-dump-server`

- Dumpolja az adatokat egy HTML-fájlba:

`var-dump-server --format=html > {{path/to/file.html}}`

- A kiszolgálót egy adott címre és portra figyelni:

`var-dump-server --host {{127.0.0.1:9912}}`
