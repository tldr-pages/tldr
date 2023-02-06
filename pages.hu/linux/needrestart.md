# needrestart

> Ellenőrizze, hogy mely démonokat kell újraindítani a könyvtárak frissítése után. További információ: <https://github.com/liske/needrestart>.

- Az elavult folyamatok listázása:

`needrestart`

- A szolgáltatások interaktív újraindítása:

`sudo needrestart`

- Az elavult folyamatok listázása \[v\]erbose vagy \[q\]uiet módban:

`needrestart -{{v|q}}`

- Ellenőrizze, hogy a \[k\]ernel elavult-e:

`needrestart -k`

- Ellenőrizze, hogy a CPU mikrokódja elavult-e:

`needrestart -w`

- Az elavult folyamatok listázása \[b\]atch módban:

`needrestart -b`

- Egy adott \[c\]onfigurációs fájl segítségével feldolgozott elavult folyamatok listázása:

`needrestart -c {{path/to/config}}`

- Súgó megjelenítése:

`needrestart --help`
