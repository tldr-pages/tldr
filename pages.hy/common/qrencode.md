# qrencode

> QR կոդի գեներատոր: Աջակցում է PNG և EPS:.
> Տես նաև՝ `qr`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/qrencode>:.

- Փոխակերպեք տողը QR կոդի և պահեք ելքային ֆայլում.:

`qrencode {{[-o|--output]}} {{path/to/output_file.png}} {{string}}`

- Փոխակերպեք մուտքային ֆայլը QR կոդի և պահեք ելքային ֆայլի մեջ.:

`qrencode {{[-o|--output]}} {{path/to/output_file.png}} {{[-r|--read-from]}} {{path/to/input_file}}`

- Փոխակերպեք տողը QR կոդի և տպեք այն տերմինալում.:

`qrencode {{[-t|--type]}} ansiutf8 {{string}}`

- Փոխարկեք մուտքագրումը խողովակից QR կոդ և տպեք այն տերմինալում.:

`echo {{string}} | qrencode {{[-t|--type]}} utf8`
