# rename

> Több fájl átnevezése. MEGJEGYZÉS: ez az oldal a `prename` Fedora csomagban található parancsra hivatkozik. További információ: <https://manned.org/man/prename>.

- Fájlok átnevezése Perl Common Regular Expression használatával (a 'foo'-t 'bar'-ral helyettesítsük, ahol csak találunk):

`rename {{'s/foo/bar/'}} {{*}}`

- Dry-run - megjeleníti, hogy mely átnevezések történnének meg anélkül, hogy végrehajtaná azokat:

`rename -n {{'s/foo/bar/'}} {{*}}`

- Átnevezés kikényszerítése még akkor is, ha a művelet eltávolítaná a meglévő célfájlokat:

`rename -f {{'s/foo/bar/'}} {{*}}`

- A fájlnevek kisbetűvé alakítása (használja a `-f` címet nagybetű-érzékeny fájlrendszerekben a "már létezik" hibák elkerülése érdekében):

`rename 'y/A-Z/a-z/' {{*}}`

- A szóközöket aláhúzásokkal helyettesíti:

`rename 's/\s+/_/g' {{*}}`
