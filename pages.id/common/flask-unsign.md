# flask-unsign

> Alat untuk melakukan brute-force, mendeskripsi (decode), dan membuat cookie sesi Flask.
> Informasi lebih lanjut: <https://github.com/Paradoxis/Flask-Unsign>.

- Mendekode cookie sesi Flask:

`flask-unsign {{[-d|--decode]}} {{[-c|--cookie]}} {{cookie}}`

- Mendekode cookie sesi yang diambil dari URL yang mengembalikan header `Set-Cookie`:

`flask-unsign {{[-d|--decode]}} --server {{URL}}`

- Melakukan brute-force kunci rahasia (secret key) menggunakan wordlist bawaan flask-unsign (membutuhkan `flask-unsign-wordlist`):

`flask-unsign {{[-u|--unsign]}} {{[-c|--cookie]}} {{cookie}}`

- Melakukan brute-force kunci rahasia dengan wordlist kustom (gunakan `--no-literal-eval` untuk entri tanpa tanda kutip):

`flask-unsign {{[-u|--unsign]}} {{[-c|--cookie]}} {{cookie}} {{[-w|--wordlist]}} {{jalan/ke/wordlist.txt}}`

- Menandatangani (sign) cookie sesi baru dengan kunci rahasia:

`flask-unsign {{[-s|--sign]}} {{[-c|--cookie]}} "{{{'logged_in': False}}}" {{[-S|--secret]}} {{rahasia}}`

- Menandatangani cookie sesi menggunakan timestamp lama/legacy (berguna untuk versi lama):

`flask-unsign {{[-s|--sign]}} {{[-c|--cookie]}} "{{{'logged_in': False}}}" {{[-S|--secret]}} {{rahasia}} {{[-l|--legacy]}}`

- Melakukan brute-force cookie sesi dengan thread kustom dan tanpa evaluasi literal:

`flask-unsign {{[-u|--unsign]}} {{[-c|--cookie]}} {{cookie}} {{[-w|--wordlist]}} {{jalan/ke/wordlist.txt}} {{[-t|--threads]}} {{jumlah_thread}} {{[-nE|--no-literal-eval]}}`
