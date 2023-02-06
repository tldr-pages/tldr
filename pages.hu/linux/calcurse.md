# calcurse

> Szövegalapú naptár és ütemező alkalmazás a parancssorhoz. További információ: <https://calcurse.org>.

- A calcurse indítása interaktív módban:

`calcurse`

- Az aktuális napra vonatkozó találkozók és események kinyomtatása és kilépés:

`calcurse --appointment`

- Az összes helyi calcurse elem eltávolítása és távoli objektumok importálása:

`calcurse-caldav --init=keep-remote`

- Az összes távoli objektum eltávolítása és a helyi calcurse-elemek betolása:

`calcurse-caldav --init=keep-local`

- Helyi objektumok másolása a CalDAV-kiszolgálóra és fordítva:

`calcurse-caldav --init=two-way`
