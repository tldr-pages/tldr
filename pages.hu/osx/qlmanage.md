# qlmanage

> QuickLook kiszolgálóeszköz. További információ: <https://ss64.com/osx/qlmanage.html>.

- QuickLook megjelenítése egy vagy több fájlhoz:

`qlmanage -p {{filename}} {{filename2}}`

- Az aktuális könyvtárban található összes JPEG fájl 300px széles PNG miniatűrjének kiszámítása és elhelyezése egy könyvtárban:

`qlmanage {{*.jpg}} -t -s {{300}} {{path/to/directory}}`

- QuickLook visszaállítása:

`qlmanage -r`
