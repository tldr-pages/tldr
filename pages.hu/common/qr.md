# qr

> QR-kódok generálása a terminálon ANSI VT-100 escape kódokkal. További információ: <https://github.com/lincolnloop/python-qrcode/>.

- QR-kód generálása:

`echo "{{data}}" | qr`

- Adja meg a hibajavítási szintet (alapértelmezett érték M):

`echo "{{data}}" | qr --error-correction={{L|M|Q|H}}`
