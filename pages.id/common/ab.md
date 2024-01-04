# ab

> Alat penguji server HTTP Apache.
> Informasi lebih lanjut: <https://httpd.apache.org/docs/current/programs/ab.html>.

- Jalankan 100 permintaan HTTP GET menuju alamat URL yang ditentukan:

`ab -n 100 {{url}}`

- Jalankan 100 permintaan HTTP GET, dikelompokkan dalam masing-masing batch berisi 10, menuju alamat URL yang ditentukan:

`ab -n 100 -c 10 {{url}}`

- Jalankan 100 perintaan HTTP POST menuju alamat URL, menggunakan data JSON yang dimuat dari file yang ditentukan:

`ab -n 100 -T {{application/json}} -p {{jalan/menuju/file.json}} {{url}}`

- Gunakan opsi HTTP [k]eep-Alive, yakni jalankan permintaan majemuk dalam satu sesi HTTP yang sama:

`ab -k {{url}}`

- Alokasikan wak[t]u maksimum (dalam hitungan detik) untuk mengujinya:

`ab -t {{60}} {{url}}`
