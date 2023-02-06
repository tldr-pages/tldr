# checkinstall

> Nyomon követi egy szoftvercsomag helyi telepítését, és olyan bináris csomagot készít, amely a rendszer natív csomagkezelőjével használható. További információ: <http://checkinstall.izto.org>.

- Csomag létrehozása és telepítése alapértelmezett beállításokkal:

`sudo checkinstall --default`

- Csomag létrehozása, de nem telepítése:

`sudo checkinstall --install={{no}}`

- Dokumentáció nélküli csomag létrehozása:

`sudo checkinstall --nodoc`

- Csomag létrehozása és a név beállítása:

`sudo checkinstall --pkgname {{package}}`

- Csomag létrehozása és a mentési hely megadása:

`sudo checkinstall --pakdir {{path/to/directory}}`
