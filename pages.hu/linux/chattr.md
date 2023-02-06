# chattr

> Fájlok vagy könyvtárak attribútumainak módosítása. További információ: <https://manned.org/chattr>.

- Egy fájl vagy könyvtár megváltoztathatatlanná tétele a változtatásokkal és törlésekkel szemben, még a szuperfelhasználó által is:

`chattr +i {{path/to/file_or_directory}}`

- Egy fájl vagy könyvtár megváltoztathatóvá tétele:

`chattr -i {{path/to/file_or_directory}}`

- Egy teljes könyvtár és tartalma rekurzív módon változtathatatlanná tétele:

`chattr -R +i {{path/to/directory}}`
