# tar

> Utilitar de arhivare.
> Adesea combinate cu o metodă de compresie, cum ar fi gzip sau bzip2.
> Mai multe informaţii: <https://www.gnu.org/software/tar>

- [c] refaceți o arhivă și scrieți-o într-o [f] ile:

`tar cf {{target.tar}} {{file1}} {{file2}} {{file3}}`

- [c] reați o g [z] arhivă și scrieți-o la o [f] ile:

`tar czf {{target.tar.gz}} {{file1}} {{file2}} {{file3}}`

- [c] reate o g [z] uitat arhiva dintr-un director folosind căi relative:

`tar czf {{target.tar.gz}} --directory={{path/to/directory}} .`

- E [x] traduce o arhivă (comprimată) [f] ile în directorul curent [v] erbosely:

`tar xvf {{source.tar[.gz|.bz2|.xz]}}`

- E [x] introduce o arhivă (comprimată) [f] ile în directorul țintă:

`tar xf {{source.tar[.gz|.bz2|.xz]}} --directory={{directory}}`

- [c] refaceți o arhivă comprimată și scrieți-o într-o [f] ile, folosind [a] sufixul rchive pentru a determina programul de compresie:

`tar caf {{target.tar.xz}} {{file1}} {{file2}} {{file3}}`

- Lis [t] conținutul gudronului [f] ile [v] erbosely:

`tar tvf {{source.tar}}`

- E [x] fișiere tract care se potrivesc cu un model dintr-o arhivă [f] ile:

`tar xf {{source.tar}} --wildcards "{{*.html}}"`
