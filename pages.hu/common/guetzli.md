# guetzli

> JPEG képtömörítő segédprogram. További információ: <https://github.com/google/guetzli>.

- JPEG kép tömörítése:

`guetzli {{input.jpg}} {{output.jpg}}`

- Tömörített JPEG kép létrehozása egy PNG képből:

`guetzli {{input.png}} {{output.jpg}}`

- A kívánt vizuális minőségű JPEG-kép tömörítése (84-100):

`guetzli --quality {{quality_value}} {{input.jpg}} {{output.jpg}}`
