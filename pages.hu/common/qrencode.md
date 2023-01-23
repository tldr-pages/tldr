# qrencode

> QR-kód generátor. Támogatja a PNG és EPS formátumokat. További információ: <https://fukuchi.org/works/qrencode>.

- Konvertáljon egy karakterláncot QR-kóddá, és mentse el egy kimeneti fájlba:

`qrencode -o {{path/to/output_file.png}} {{string}}`

- Egy bemeneti fájl átalakítása QR-kóddá és mentése kimeneti fájlba:

`qrencode -o {{path/to/output_file.png}} -r {{path/to/input_file}}`

- Egy karakterlánc átalakítása QR-kóddá és kinyomtatása terminálon:

`qrencode -t ansiutf8 {{string}}`

- Bemenet konvertálása pipából QR-kóddá és kinyomtatása terminálban:

`echo {{string}} | qrencode -t ansiutf8`
