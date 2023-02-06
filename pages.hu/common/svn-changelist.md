# svn changelist

> Változáslista társítása egy fájlkészlethez. További információ: <http://svnbook.red-bean.com/en/1.7/svn.advanced.changelists.html>.

- Fájlok hozzáadása egy changelistához, létrehozva a changelistát, ha az nem létezik:

`svn changelist {{changelist_name}} {{path/to/file1}} {{path/to/file2}}`

- Fájlok eltávolítása egy változtatási listából:

`svn changelist --remove {{path/to/file1}} {{path/to/file2}}`

- Az egész changelistát egyszerre távolítja el:

`svn changelist --remove --recursive --changelist {{changelist_name}} .`

- Könyvtárak szóközzel elválasztott listájának tartalmának hozzáadása egy változtatási listához:

`svn changelist --recursive {{changelist_name}} {{path/to/directory1}} {{path/to/directory2}}`

- Egy változtatási lista átadása:

`svn commit --changelist {{changelist_name}}`
