# date

> Mengatur atau menampilkan tanggal sistem.
> Informasi lebih lanjut: <https://ss64.com/osx/date.html>.

- Menampilkan tanggal saat ini menggunakan format _locale_:

`date +"%c"`

- Menampilkan tanggal saat ini dalam format UTC and ISO 8601:

`date -u +"%Y-%m-%dT%H:%M:%SZ"`

- Menampilkan tanggal saat ini sebagai _Unix timestamp_ (detik sejak jaman Unix):

`date +%s`

- Menampilkan tanggal tertentu (diwakili sebagai _Unix timestamp_) menggunakan format bawaan:

`date -r 1473305798`
