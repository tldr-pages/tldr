# entr

> Tetszőleges parancsok futtatása a fájlok változásakor. További információ: <https://manned.org/entr>.

- Újraépítés a `make` címmel, ha bármelyik alkönyvtárban bármelyik fájl megváltozik:

`{{ag -l}} | entr {{make}}`

- Újraépítés és tesztelés a `make` segítségével, ha az aktuális könyvtárban lévő bármelyik `.c` forrásfájl megváltozik:

`{{ls *.c}} | entr {{'make && make test'}}`

- Küldjön egy `SIGTERM` üzenetet a `ruby main.rb` végrehajtása előtt bármely korábban indított ruby alfolyamatnak:

`{{ls *.rb}} | entr -r {{ruby main.rb}}`

- Futtasson egy parancsot a megváltozott fájl (`/_`) argumentumával:

`{{ls *.sql}} | entr {{psql -f}} /_`
