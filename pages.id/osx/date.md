# date

> Atur atau tampilkan tanggal sistem.
> Informasi lebih lanjut: <https://keith.github.io/xcode-man-pages/date.1.html>.

- Tampilkan tanggal saat ini menggunakan format _locale_:

`date +%c`

- Tampilkan tanggal saat ini dalam format UTC and ISO 8601:

`date -u +%Y-%m-%dT%H:%M:%SZ`

- Tampilkan tanggal saat ini sebagai _Unix timestamp_ (detik sejak jaman Unix):

`date +%s`

- Tampilkan tanggal tertentu (diwakili sebagai _Unix timestamp_) menggunakan format bawaan:

`date -r {{1473305798}}`
