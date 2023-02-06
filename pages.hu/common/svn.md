# svn

> Subversion parancssori kliens eszköz. További információ: <https://subversion.apache.org>.

- Egy munkakópia megtekintése egy tárolóból:

`svn co {{url/to/repository}}`

- A tárolóból származó változtatások átvitele a munkakópiába:

`svn up`

- Fájlok és könyvtárak verziókezelés alá helyezése, ütemezés a tárolóba való felvételre. A következő commitban kerülnek hozzáadásra:

`svn add {{PATH}}`

- A munkakópiából a változtatások elküldése a tárolóba:

`svn ci -m {{commit_log_message}} [{{PATH}}]`

- Az utolsó 10 revízió változásainak megjelenítése, a módosított fájlok megjelenítése minden egyes revízióhoz:

`svn log -vl {{10}}`

- Részletes súgó megjelenítése:

`svn help`
