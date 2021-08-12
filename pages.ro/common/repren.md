# repren

> Instrument de înlocuire șir multi-model și redenumire fișier.
> Mai multe informaţii: <https://github.com/jlevy/repren>

- Redenumiți un șir uscat un director de pngs cu un șir de înlocuire literală:

`repren --dry-run --rename --literal --from '{{find_string}}' --to '{{replacement_string}}' {{*.png}}`

- Faceți o executare uscată redenumiți un director de jpegs cu o expresie regulată:

`repren --rename --dry-run --from '{{regular_expression}}' --to '{{replacement_string}}' {{*.jpg}} {{*.jpeg}}`

- Faceți o găsire-și-înlocuire pe conținutul unui director de fișiere csv:

`repren --from '{{([0-9]+) example_string}}' --to '{{replacement_string \1}}' {{*.csv}}`

- Faceți atât o operațiune de găsire și înlocuire, cât și o operațiune de redenumire în același timp, utilizând un fișier tipar:

`repren --patterns {{path/to/patfile.ext}} --full {{*.txt}}`

- Faceți o redenumire insensibilă la majuscule:

`repren --rename --insensitive --patterns {{path/to/patfile.ext}} *`
