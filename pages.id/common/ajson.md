# ajson

> Jalankan ekspresi pencarian JSONPath terhadap objek-objek JSON.
> Informasi lebih lanjut: <https://github.com/spyzhov/ajson>.

- Baca file JSON dan jalankan ekpresi JSONPath untuk mencari data di dalamnya:

`ajson '{{$..json[?(@.path)]}}' {{jalan/menuju/file.json}}`

- Baca JSON dari `stdin` dan jalankan ekpresi JSONPath untuk mencari data di dalamnya:

`cat {{jalan/menuju/file.json}} | ajson '{{$..json[?(@.path)]}}'`

- Baca JSON dari sebuah URL dan jalankan ekpresi JSONPath untuk mencari data di dalamnya:

`ajson '{{avg($..price)}}' '{{https://example.com/api/}}'`

- Baca file JSON sederhana dan hitung nilai dari ekspresi JSONPath:

`echo '{{3}}' | ajson '{{2 * pi * $}}'`
