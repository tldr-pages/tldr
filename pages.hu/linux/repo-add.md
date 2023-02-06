# repo-add

> Csomagadatbázis karbantartó segédprogram, amely lehetővé teszi az említett csomagok telepítését a Pacman segítségével. További információ: <https://man.archlinux.org/man/repo-add>.

- Hozzáadja az összes csomag binárisát az aktuális könyvtárban, és eltávolítja a régi adatbázisfájlt:

`repo-add --remove {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`

- Az aktuális könyvtárban lévő összes csomag bináris állományának hozzáadása csendes üzemmódban, kivéve a figyelmeztető és hibaüzeneteket:

`repo-add --quiet {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`

- Az aktuális könyvtárban lévő összes csomag bináris állományának hozzáadása színjelzés nélkül:

`repo-add --nocolor {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`
