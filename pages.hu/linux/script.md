# script

> A terminál összes kimenetének rögzítése fájlba. További információ: <https://manned.org/script>.

- Új munkamenet rögzítése az aktuális könyvtárban található `typescript` nevű fájlba:

`script`

- Új munkamenet rögzítése egy egyéni fájlútvonalra:

`script {{path/to/session.out}}`

- Új munkamenet rögzítése egy meglévő fájlhoz csatolva:

`script -a {{path/to/session.out}}`

- Időzítési információk rögzítése (az adatok a standard hibaüzenetbe kerülnek):

`script -t 2> {{path/to/timingfile}}`
