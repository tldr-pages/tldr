# qr

> Generați coduri QR în terminal cu codurile de evacuare ANSI VT-100.
> Mai multe informaţii: <https://github.com/lincolnloop/python-qrcode/>

- Generează un cod QR:

`echo "{{data}}" | qr`

- Specificați nivelul de corecție a erorilor (implicit la M):

`echo "{{data}}" | qr --error-correction={{L|M|Q|H}}`
