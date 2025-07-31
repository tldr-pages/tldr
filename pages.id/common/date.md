# date

> Tetapkan atau tampilkan tanggal sistem.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/date-invocation.html>.

- Menampilkan tanggal saat ini menggunakan format lokal default:

`date +%c`

- Menampilkan tanggal saat ini dalam UTC, menggunakan format ISO 8601:

`date {{[-u|--utc]}} +%Y-%m-%dT%H:%M:%S%Z`

- Menampilkan tanggal saat ini sebagai stempel waktu Unix (detik sejak zaman Unix):

`date +%s`

- Mengonversi tanggal yang ditentukan sebagai stempel waktu Unix ke format default:

`date {{[-d|--date]}} @{{1473305798}}`

- Konversi tanggal yang diberikan ke format stempel waktu Unix:

`date {{[-d|--date]}} "{{2018-09-01 00:00}}" +%s {{[-u|--utc]}}`

- Menampilkan tanggal saat ini menggunakan format RFC-3339 (`YYYY-MM-DD hh:mm:ss TZ`):

`date --rfc-3339 s`

- Tetapkan tanggal saat ini menggunakan format `MMDDhhmmYYYY.ss` (`YYYY` and `.ss` are optional):

`date {{093023592021.59}}`

- Menampilkan nomor minggu ISO saat ini:

`date +%V`
