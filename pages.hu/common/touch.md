# touch

> Fájlok létrehozása és hozzáférési/módosítási idők beállítása. További információ: <https://manned.org/man/freebsd-13.1/touch>.

- Speciális fájlok létrehozása:

`touch {{path/to/file1 path/to/file2 ...}}`

- Állítsa be a fájl \[a\]hozzáférési vagy \[m\]odifikációs idejét az aktuálisra, és ne \[c\]indítsa el a fájlt, ha az nem létezik:

`touch -c -{{a|m}} {{path/to/file1 path/to/file2 ...}}`

- Állítsa be a fájl \[t\]ime értékét egy adott értékre, és ne \[c\]reate fájl, ha nem létezik:

`touch -c -t {{YYYYMMDDHHMM.SS}} {{path/to/file1 path/to/file2 ...}}`

- Állítsa be egy adott fájl fájlidejét egy másik \[r\] fájl idejére, és ne \[c\]reate fájl, ha nem létezik:

`touch -c -r {{~/.emacs}} {{path/to/file1 path/to/file2 ...}}`
