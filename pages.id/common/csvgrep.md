# csvgrep

> Filter baris-baris CSV menggunakan pencocokan string dan pola (pattern matching).
> Bagian dari csvkit.
> Informasi lebih lanjut: <https://csvkit.readthedocs.io/en/latest/scripts/csvgrep.html>.

- Temukan baris-baris yang memiliki string tertentu pada kolom 1:

`csvgrep {{[-c|--columns]}} {{1}} {{[-m|--match]}} {{string_to_match}} {{data.csv}}`

- Temukan baris-baris di mana isi kolom 3 atau 4 cocok dengan ekspresi reguler (`regex`) tertentu:

`csvgrep {{[-c|--columns]}} {{3,4}} {{[-r|--regex]}} {{regex}} {{data.csv}}`

- Temukan baris-baris di mana kolom "nama" TIDAK memuat string "John Doe":

`csvgrep {{[-i|--invert-match]}} {{[-c|--columns]}} {{nama}} {{[-m|--match]}} "{{John Doe}}" {{data.csv}}`
