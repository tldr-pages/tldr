# ctrlaltdel

> Segédprogram annak vezérlésére, hogy mi történjen a CTRL+ALT+DEL billentyűkombináció megnyomásakor. További információ: <https://manned.org/ctrlaltdel>.

- Jelenlegi beállítások lekérdezése:

`ctrlaltdel`

- A CTRL+ALT+DEL beállítása az azonnali újraindításhoz, minden előkészület nélkül:

`sudo ctrlaltdel hard`

- A CTRL+ALT+DEL beállítása "normál" újraindításhoz, lehetőséget adva a folyamatoknak, hogy előbb kilépjenek (SIGINT-et küldjön a PID1-re):

`sudo ctrlaltdel soft`
