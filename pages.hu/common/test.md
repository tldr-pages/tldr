# test

> A fájltípusok ellenőrzése és az értékek összehasonlítása. 0-t ad vissza, ha a feltétel igaz, 1-et, ha hamis. További információ: <https://www.gnu.org/software/coreutils/test>.

- Annak vizsgálata, hogy egy adott változó egyenlő-e egy adott karakterlánccal:

`test "{{$MY_VAR}}" == "{{/bin/zsh}}"`

- Annak tesztelése, hogy egy adott változó üres-e:

`test -z "{{$GIT_BRANCH}}"`

- Teszteli, hogy létezik-e egy fájl:

`test -f "{{path/to/file_or_directory}}"`

- Teszteli, hogy egy könyvtár nem létezik-e:

`test ! -d "{{path/to/directory}}"`

- Ha A igaz, akkor B, vagy hiba esetén C (vegyük észre, hogy a C akkor is lefuthat, ha A sikertelen):

`test {{condition}} && {{echo "true"}} || {{echo "false"}}`
