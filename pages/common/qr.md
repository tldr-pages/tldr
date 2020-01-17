# qr

> Generate QR codes in the terminal with ANSI VT-100 escape codes.
> More information: <https://github.com/lincolnloop/python-qrcode/>.

- Generate a QR code:

`echo "{{data}}" | qr`

- Specify the error correction level (defaults to M):

`echo "{{data}}" | qr --error-correction={{L|M|Q|H}}`
