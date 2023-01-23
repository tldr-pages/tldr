# echo

> Megadott argumentumok nyomtatása. További információ: <https://www.gnu.org/software/coreutils/echo>.

- Szöveges üzenet nyomtatása. Megjegyzés: az idézőjelek opcionálisak:

`echo "{{Hello World}}"`

- Üzenet nyomtatása a környezeti változókkal:

`echo "{{My path is $PATH}}"`

- Üzenet nyomtatása az utolsó újsor nélkül:

`echo -n "{{Hello World}}"`

- Üzenet csatolása a fájlhoz:

`echo "{{Hello World}}" >> {{file.txt}}`

- A backslash-ek (speciális karakterek) értelmezésének engedélyezése:

`echo -e "{{Column 1\tColumn 2}}"`
