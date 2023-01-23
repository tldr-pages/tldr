# tar

> Gyakran kombinálják tömörítési módszerrel, például gzip vagy bzip2. További információ: <https://www.gnu.org/software/tar>.

- \[c\]reate an archive and write it to a \[f\]ile:

`tar cf {{target.tar}} {{file1}} {{file2}} {{file3}}`

- \[c\]reate a g\[z\]ipped archive and write it to a \[f\]ile:

`tar czf {{target.tar.gz}} {{file1}} {{file2}} {{file3}}`

- \[c\]reate a g\[z\]ipped archive from a directory using relative paths:

`tar czf {{target.tar.gz}} --directory={{path/to/directory}} .`

- E\[x\]tract a (tömörített) archívum \[f\]ile az aktuális könyvtárba \[v\]erbosely:

`tar xvf {{source.tar[.gz|.bz2|.xz]}}`

- E\[x\]tract a (tömörített) archívum \[f\]ile a célkönyvtárba:

`tar xf {{source.tar[.gz|.bz2|.xz]}} --directory={{path/to/directory}}`

- \[c\]reate a tömörített archívum és írja ki egy \[f\]ile fájlba, a \[a\]rchive utótagot használva a tömörítőprogram meghatározásához:

`tar caf {{target.tar.xz}} {{file1}} {{file2}} {{file3}}`

- Egy tar \[f\]ile tartalmának \[v\]erbosely \[v\]erbosely:

`tar tvf {{source.tar}}`

- E\[x\]tract fájlokat egy archív \[f\]ile-ről, amelyek megfelelnek egy mintának:

`tar xf {{source.tar}} --wildcards "{{*.html}}"`
