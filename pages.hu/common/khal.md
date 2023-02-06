# khal

> Szövegalapú naptár és ütemező alkalmazás a parancssorhoz. További információ: <https://lostpackets.de/khal>.

- Indítsa el a khal-t interaktív módban:

`ikhal`

- A személyes naptárban a következő hét napra tervezett összes esemény kinyomtatása:

`khal list -a {{personal}} {{today}} {{7d}}`

- A holnap 10:00 órára tervezett, nem a személyes naptárban szereplő összes esemény kinyomtatása:

`khal at -d {{personal}} {{tomorrow}} {{10:00}}`

- A következő három hónapra tervezett események listáját tartalmazó naptár nyomtatása:

`khal calendar`

- Új esemény hozzáadása a személyes naptárhoz:

`khal new -a {{personal}} {{2020-09-08}} {{18:00}} {{18:30}} "{{Dentist appointment}}"`
