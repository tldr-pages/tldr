# bc

> Suatu bahasa kalkulator presisi.
> Lihat juga: `dc`, `qalc`.
> Informasi lebih lanjut: <https://manned.org/bc>.

- Jalankan sesi interaktif baru:

`bc`

- Jalankan sesi interaktif dengan memuat pustaka dasar matematika:

`bc {{[-i|--interactive]}} {{[-l|--mathlib]}}`

- Lakukan penghitungan terhadap suatu pernyataan:

`echo '{{5 / 3}}' | bc`

- Jalankan suatu berkas skrip:

`bc {{jalan/menuju/skrip.bc}}`

- Hitung hasil suatu pernyataan dengan skala desimal tertentu:

`echo 'scale = {{10}}; {{5 / 3}}' | bc`

- Hitung hasil [s]inus, [c]osinus, [a]rctangen, atau [l]ogaritma/[e]ksponensi natural atas suatu bilangan menggunakan `mathlib`:

`echo '{{s|c|a|l|e}}({{1}})' | bc {{[-l|--mathlib]}}`

- Jalankan suatu skrip perhitungan faktorial secara sebaris:

`echo "define factorial(n) { if (n <= 1) return 1; return n*factorial(n-1); }; factorial({{10}})" | bc`
