# pacdiff

> Karbantartó segédprogram a `.pacorig`, `.pacnew` és `.pacsave` fájlok számára, amelyeket a `pacman` hozott létre. További információ: <https://man.archlinux.org/man/pacdiff>.

- Tekintse át a karbantartást igénylő fájlokat interaktív módban:

`pacdiff`

- Használja a sudo és a sudoedit parancsokat a fájlok eltávolításához és egyesítéséhez:

`pacdiff --sudo`

- Tekintse át a karbantartást igénylő fájlokat, és hozzon létre `.bak`feloldásokat az eredetiből, ha `(O)verwrite`:

`pacdiff --sudo --backup`

- Egy adott szerkesztő használata a konfigurációs fájlok megtekintéséhez és egyesítéséhez (alapértelmezett a `vim -d`):

`DIFFPROG={{editor}} pacdiff`

- A konfigurációs fájlok keresése a `locate` segítségével a pacman adatbázis használata helyett:

`pacdiff --locate`

- Súgó megjelenítése:

`pacdiff --help`
