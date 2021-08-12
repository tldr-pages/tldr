# qrencode

> Generator de coduri QR. Suportă PNG și EPS.
> Mai multe informaţii: <https://fukuchi.org/works/qrencode>

- Convertiți un șir la un cod QR și salvați într-un fișier de ieșire:

`qrencode -o {{path/to/output_file.png}} {{string}}`

- Convertiți un fișier de intrare într-un cod QR și salvați într-un fișier de ieșire:

`qrencode -o {{path/to/output_file.png}} -r {{path/to/input_file}}`

- Conversia unui șir la un cod QR și imprimați-l în terminal:

`qrencode -t ansiutf8 {{string}}`

- Conversia de intrare de la țeavă la un cod QR și imprimați-l în terminal:

`echo {{string}} | qrencode -t ansiutf8`
