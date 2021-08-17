# tar

> Utilitar de arhivare.
> Adesea combinate cu o metodă de compresie, cum ar fi gzip sau bzip2.
> Mai multe informaţii: <https://www.gnu.org/software/tar>

- [c]reați o arhivă și scrieți-o într-un [f]ișier:

`tar cf {{target.tar}} {{file1}} {{file2}} {{file3}}`

- [c]reați o [z] arhivă comprimată și scrieți-o într-un [f]ișier:

`tar czf {{target.tar.gz}} {{file1}} {{file2}} {{file3}}`

- [c]reați o [z] arhivă comprimată dintr-un director folosind căi relative:

`tar czf {{target.tar.gz}} --directory={{path/to/directory}} .`

- E[x]trage o arhivă (comprimată) din [f]ișier în directorul curent cu [v]erbositate:

`tar xvf {{source.tar[.gz|.bz2|.xz]}}`

- E[x]trage o arhivă (comprimată) din [f]ișier în directorul țintă:

`tar xf {{source.tar[.gz|.bz2|.xz]}} --directory={{directory}}`

- [c]reați o arhivă comprimată și scrieți-o într-un [f]ișier, folosind sufixul [a]arhivă pentru a determina programul de compresie:

`tar caf {{target.tar.xz}} {{file1}} {{file2}} {{file3}}`

- Lis[t]ați conținutul arhivei din [f]ișier cu [v]verbositate:

`tar tvf {{source.tar}}`

- E[x]trage fișiere care se potrivesc cu un model dintr-o arhivă din [f]ișier:

`tar xf {{source.tar}} --wildcards "{{*.html}}"`
